# 🐾 Animal Skin Disease Classifier API

This project is a FastAPI-based backend that classifies common skin conditions in dogs, cats, and cows using pre-trained TensorFlow/Keras models.  
It also provides medicine suggestions for the predicted disease using Gemini (via `med.py`).  
**NOTE:** Create and load your own Gemini API key before running the app.

---

## 🚀 Features
- Image upload support (.jpg, .png, .jpeg)
- Lazy model loading for efficient memory usage
- Supported animals:
  - 🐶 Dogs → Demodicosis, Dermatitis, Fungal Infection, Hypersensitivity, Ringworm, Healthy
  - 🐱 Cats → Flea Allergy, Ringworm, Scabies, Healthy
  - 🐄 Cows → Lumpy Skin, Healthy
- Normalizes inconsistent labels
- Fetches medicine suggestions using Gemini

---

## 📂 Project Structure
```plaintext
.
├── app.py              # Streamlit frontend
├── main.py             # FastAPI backend
├── model_loader.py     # Handles lazy loading of Keras models
├── utils.py            # Utility functions (image preprocessing)
├── med.py              # Gemini API integration
├── Dog.keras           # Pre-trained dog model
├── cat.keras           # Pre-trained cat model
├── cow.keras           # Pre-trained cow model
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment config
└── README.md           # Documentation


git clone https://github.com/ankitkr1375/animal_classifier.git
cd animal_classifier

python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
streamlit run app.py


