import pickle 
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/model_smotenc-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

classes = {0: "hate speech", 1: "offensive speech ", 2: "neutral"}

def predict(text: str) -> str:
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return classes[model.predict([text])[0]]