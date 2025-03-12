import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO

classifier = pipeline("image-classification", model="Vampyrian/buitine-technika-ir-elektronika")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins, you can use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"]  # Allow all headers
)


class ImagePrompt(BaseModel):
    image_url: str

@app.get("/")
def read_root():
    return {"Heartbeat": "I am still alive!"}

@app.post("/predict/image/buitine-technika-ir-elektronika")
def read_item(data: ImagePrompt):
    image_url = data.image_url

    response = requests.get(image_url)
    response.raise_for_status()  # Ensure the request was successful
    image = Image.open(BytesIO(response.content))
    res = classifier(image)

    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)