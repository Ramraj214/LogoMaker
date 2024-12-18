FROM python:3.11-slim

WORKDIR /Logo_maker/backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="/usr/local/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]