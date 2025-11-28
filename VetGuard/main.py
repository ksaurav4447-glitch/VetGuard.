from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from model_loader import get_model
from utils import read_image
import tensorflow as tf
import numpy as np
from med import get_medicine_suggestion

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASS_NAMES = {
    "dog": ["Demodicosis", "Dermatitits", "Fungal_Infection", "Healthy", "Hypersenstivity", "Ringworm"],
    "cat": ["Flea_Allergy", "Health", "Ringworm", "Scabies"],
    "cow": ["Lumpy Skin", "Normal Skin"]
}

@app.post("/predict/")
async def predict(
    animal_type: str = Form(...),
    file: UploadFile = File(...)
):
    if animal_type not in CLASS_NAMES:
        raise HTTPException(
            status_code=400, detail="Invalid animal_type. Choose dog, cat, cow."
        )

    # Read image bytes
    image_bytes = await file.read()
    img_array = read_image(image_bytes)

    # Load model based on animal type
    model = get_model(animal_type)

    # Predict
    prediction = model.predict(np.expand_dims(img_array, axis=0))
    label_index = np.argmax(prediction)
    label = CLASS_NAMES[animal_type][label_index]

    # Normalize Labels
    if label in ["Health", "Lumpy Skin"]:
        label = "Healthy"
    if label == "Flea_Allergy":
        label = "Flea Allergy"
    if label == "Fungal_infections":
        label = "Fungal Infections"

    # Medicine Suggestion
    try:
        medicine_suggestion = get_medicine_suggestion(label, animal_type)
    except Exception as e:
        medicine_suggestion = f"Failed to fetch suggestion: {str(e)}"

    return JSONResponse(content={
        "disease": label,
        "medicine": medicine_suggestion
    })
