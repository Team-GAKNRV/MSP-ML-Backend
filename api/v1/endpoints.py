import os
import uuid

from fastapi import APIRouter, File, UploadFile
from core.scripts.classification import classify_single_label
from core.scripts.constants import CLASSIFIED_LABELS_ARRAY, LAYERS_ARTICLE_TYPE, LAYERS_BASE_COLOUR, LAYERS_SEASON, LAYERS_USAGE, MODEL_ARTICLE_TYPE, MODEL_BASE_COLOUR, MODEL_SEASON, MODEL_USAGE, PATH_TEMP_FILES, TAG_NAME_ARTICLE_TYPE, TAG_NAME_BASE_COLOUR, TAG_NAME_SEASON, TAG_NAME_USAGE


router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

@router.post("/classify")
async def classify_uploaded_image(input_image: UploadFile = File(...)):
    temp_file_path = f"{PATH_TEMP_FILES}/{uuid.uuid4()}.jpg"

    with open(temp_file_path, "wb") as buffer:
        buffer.write(input_image.file.read())
    
    classified_labels = CLASSIFIED_LABELS_ARRAY

    article_type = classify_single_label(MODEL_ARTICLE_TYPE, LAYERS_ARTICLE_TYPE, TAG_NAME_ARTICLE_TYPE, input_image)
    #base_colour = classify_single_label(MODEL_BASE_COLOUR, LAYERS_BASE_COLOUR, TAG_NAME_BASE_COLOUR, input_image)
    #season = classify_single_label(MODEL_SEASON, LAYERS_SEASON, TAG_NAME_SEASON, input_image)
    #usage = classify_single_label(MODEL_USAGE, LAYERS_USAGE, TAG_NAME_USAGE, input_image)

    classified_labels['articleType'] = article_type
    #classified_labels['baseColour'] = base_colour
    #classified_labels['season'] = season
    #classified_labels['usage'] = usage
    
    os.remove(temp_file_path)
    
    return classified_labels
