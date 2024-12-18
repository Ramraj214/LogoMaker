from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017/")

db_users = client["UserDB"]
user_collection = db_users["users"]

user_data = {
    "username": "Ramraj",
    "email": "ramraj@gmail.com",
    "password": "ram@123"
}

user_collection.insert_one(user_data)
print("User data inserted into UserDB.users")

db_prompts = client["PromptDB"]
prompt_collection = db_prompts["user_prompts"]

prompt = "Create a stylish logo for the text 'AP Agro since 2023'"
username = "Ramraj"

image_name = f"{username}_logo.png"

prompt_data = {
    "username": username,
    "prompt": prompt,
    "image_name": image_name
}

prompt_collection.insert_one(prompt_data)
print("Prompt and image name data inserted into PromptDB.user_prompts")

image_path = os.path.join(os.getcwd(), image_name)

with open(image_path, "wb") as img_file:
    img_file.write(b"")

print(f"Image saved as {image_name} at {image_path}")

client.close()


