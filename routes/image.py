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

@router.post("/predict/image/buitine-technika-ir-elektronika", tags=["image"])
async def buitine_technika_ir_elektronika(data: ImagePrompt):
    buitine_technika_ir_elektronika_classifier = pipeline("image-classification", model="Vampyrian/buitine-technika-ir-elektronika")

    image = get_image(data.image_url)
    return buitine_technika_ir_elektronika_classifier(image)

@router.post("/predict/image/kompiuterine-technika", tags=["image"])
async def kompiuterine_technika(data: ImagePrompt):
    kompiuterine_technika_classifier = pipeline("image-classification", model="Vampyrian/kompiuterine-technika")

    image = get_image(data.image_url)
    return kompiuterine_technika_classifier(image)

@router.post("/predict/image/telefonai", tags=["image"])
async def telefonai(data: ImagePrompt):
    telefonai_classifier = pipeline("image-classification", model="Vampyrian/telefonai")

    image = get_image(data.image_url)
    return telefonai_classifier(image)

@router.post("/predict/image/foto-ir-video", tags=["image"])
async def foto_ir_video(data: ImagePrompt):
    foto_ir_video_classifier = pipeline("image-classification", model="Vampyrian/foto-ir-video")

    image = get_image(data.image_url)
    return foto_ir_video_classifier(image)

@router.post("/predict/image/vaizdo-ir-garso-technika", tags=["image"])
async def vaizdo_ir_garso_technika(data: ImagePrompt):
    vaizdo_ir_garso_technika_classifier = pipeline("image-classification", model="Vampyrian/vaizdo-ir-garso-technika")

    image = get_image(data.image_url)
    return vaizdo_ir_garso_technika_classifier(image)

@router.post("/predict/image", tags=["image"], description="Galima spėlioti šitas kategorijas: 1) Sodui ir namams 2) sportas laisvalaikis 3) kompiuterine technika 4) vaizdas ir garsas 5) foto ir video 6) telefonai/buitine technika ir elektronika")
async def all_image_predictor(data: ImagePrompt):
    image_predictor = pipeline("image-classification", model="Vampyrian/all-images-model")

    image = get_image(data.image_url)
    return image_predictor(image)