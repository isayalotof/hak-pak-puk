from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from rapidfuzz.distance import Levenshtein
from ultralytics import YOLO
import easyocr
import cv2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
from io import BytesIO
from PIL import Image

app = FastAPI()

class ImageInput(BaseModel):
    image_base64: str

# Загрузка обученной модели YOLOv8
model = YOLO("C:\\Users\\SystemX\\PycharmProjects\\hak-pak-puk\\config_file\\best.pt")  # замените на вашу лучшую модель

# Инициализация EasyOCR
reader = easyocr.Reader(['en'])

# Функция для декодирования изображения
import numpy as np

# Функция для декодирования изображения
def decode_image(image_base64: str) -> np.ndarray:
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    image = image.convert("RGB")  # Преобразование в RGB формат для корректной обработки
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


# Функция для распознавания текста
def detect_and_recognize_text_in_image(image, model, reader, database_numbers):
    results = model(image)
    detections = results[0].boxes.xywh.tolist() if results[0].boxes else []

    img_h, img_w = image.shape[:2]
    detected_texts = []

    for box in detections:
        x_center, y_center, width, height = box[:4]
        x1, y1 = int((x_center - width / 2) * img_w), int((y_center - height / 2) * img_h)
        x2, y2 = int((x_center + width / 2) * img_w), int((y_center + height / 2) * img_h)
        cropped_image = image[y1:y2, x1:x2]
        text = reader.readtext(cropped_image, detail=0)
        detected_texts.extend(text)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    detected_number = ' '.join(detected_texts)
    best_partial_match = process.extractOne(detected_number, database_numbers, scorer=fuzz.partial_ratio)
    return best_partial_match[0] if best_partial_match else ""

# Эндпоинт для обработки изображения
@app.post("/process_image/")
async def process_image(input_data: ImageInput):
    image = decode_image(input_data.image_base64)
    database_numbers = ["example_number1", "example_number2"]  # Replace with actual database values
    result_text = detect_and_recognize_text_in_image(image, model, reader, database_numbers)
    return {"text": result_text}
