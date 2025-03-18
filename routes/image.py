from fastapi import APIRouter
from pydantic import BaseModel

from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO

router = APIRouter()

def get_image(image_url: str) -> Image:
    response = requests.get(image_url)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    return image

class ImagePrompt(BaseModel):
    image_url: str

buitine_technika_ir_elektronika_classifier = pipeline("image-classification", model="Vampyrian/buitine-technika-ir-elektronika")
kompiuterine_technika_classifier = pipeline("image-classification", model="Vampyrian/kompiuterine-technika")
telefonai_classifier = pipeline("image-classification", model="Vampyrian/telefonai")
foto_ir_video_classifier = pipeline("image-classification", model="Vampyrian/foto-ir-video")
vaizdo_ir_garso_technika_classifier = pipeline("image-classification", model="Vampyrian/vaizdo-ir-garso-technika")

@router.post("/predict/image/buitine-technika-ir-elektronika", tags=["image"])
async def buitine_technika_ir_elektronika(data: ImagePrompt):
    image = get_image(data.image_url)
    return buitine_technika_ir_elektronika_classifier(image)

@router.post("/predict/image/kompiuterine-technika", tags=["image"])
async def kompiuterine_technika(data: ImagePrompt):
    image = get_image(data.image_url)
    return kompiuterine_technika_classifier(image)

@router.post("/predict/image/telefonai", tags=["image"])
async def telefonai(data: ImagePrompt):
    image = get_image(data.image_url)
    return telefonai_classifier(image)

@router.post("/predict/image/foto-ir-video", tags=["image"])
async def foto_ir_video(data: ImagePrompt):
    image = get_image(data.image_url)
    return foto_ir_video_classifier(image)

@router.post("/predict/image/vaizdo-ir-garso-technika", tags=["image"])
async def vaizdo_ir_garso_technika(data: ImagePrompt):
    image = get_image(data.image_url)
    return vaizdo_ir_garso_technika_classifier(image)