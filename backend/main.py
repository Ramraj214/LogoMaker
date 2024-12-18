from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import requests
import io
from PIL import Image
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient("mongodb://localhost:27017/")
db_users = client["UserDB"]
user_collection = db_users["users"]

db_prompts = client["PromptDB"]
prompt_collection = db_prompts["user_prompts"]

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}


class LoginInput(BaseModel):
    identifier: str  
    password: str

class PromptInput(BaseModel):
    username: str
    prompt: str

@app.post("/signup")
def signup(username: str, email: str, password: str):
    if user_collection.find_one({"$or": [{"username": username}, {"email": email}]}):
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    user_data = {
        "username": username,
        "email": email,
        "password": password
    }
    user_collection.insert_one(user_data)
    
    return {"message": "Signup successful"}

@app.post("/login")
def login(login_input: LoginInput):
    user = user_collection.find_one({
        "$or": [{"email": login_input.identifier}, {"username": login_input.identifier}],
        "password": login_input.password
    })
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username, email, or password")
    
    return {"message": "Login successful"}


# Function to query Hugging Face API
def query_huggingface_model(prompt: str):
    # inp=f"You are logo maker that takes text as input and help to create a logo . Create a logo for {prompt}"

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error generating image")
    return response.content

@app.post("/generate")
def generate_image(prompt_input: PromptInput):
    user = user_collection.find_one({"username": prompt_input.username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate the image using Hugging Face API
    image_bytes = query_huggingface_model(prompt_input.prompt)

    # Generate a unique image name
    count=1
    while count >0:
        image_name = f"{prompt_input.username}_logo_{count}.png"
        count+=1

    # Store the prompt and image name in the database
    prompt_data = {
        "username": prompt_input.username,
        "prompt": prompt_input.prompt,
        "image_name": image_name
    }
    prompt_collection.insert_one(prompt_data)

    # Save the image locally
    image = Image.open(io.BytesIO(image_bytes))
    image_path = os.path.join(os.getcwd(), image_name)
    image.save(image_path)

    return {"message": "Image generated and saved successfully", "image_name": image_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
