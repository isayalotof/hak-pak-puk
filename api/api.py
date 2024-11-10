import requests

def ai_photo_work(image_base64):
    url = "http://127.0.0.1:8000/process_image/"
    headers = {"Content-Type": "application/json"}
    data = {
        "image_base64": image_base64
    }
    return requests.post(url, json=data, headers=headers)
