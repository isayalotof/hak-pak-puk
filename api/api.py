import requests

def ai_photo_work(image_base64):
    # Открываем изображение и конвертируем его в base64


    # Формируем запрос
    url = "http://127.0.0.1:8000/process_image/"
    headers = {"Content-Type": "application/json"}
    data = {
        "image_base64": image_base64
    }

    # Отправляем POST запрос к API
    return requests.post(url, json=data, headers=headers)


