# Проект по обработке изображений с использованием YOLO и EasyOCR

## Описание
Данный проект представляет собой веб-сервис, разработанный с использованием FastAPI, который принимает изображение в формате Base64, выполняет обнаружение объектов на основе обученной модели YOLOv8 и распознает текст на найденных объектах с помощью EasyOCR. После распознавания текста сервис возвращает наиболее подходящее совпадение из базы данных с использованием библиотеки FuzzyWuzzy для нечеткого поиска.

## Используемые технологии
- **FastAPI** — фреймворк для создания веб-приложений.
- **YOLOv8** — модель для детектирования объектов.
- **EasyOCR** — инструмент для распознавания текста на изображениях.
- **FuzzyWuzzy** — библиотека для нечеткого поиска совпадений.
- **OpenCV** — библиотека для обработки изображений.
- **Pillow (PIL)** — библиотека для работы с изображениями.
- **NumPy** — библиотека для работы с многомерными массивами.

## Установка и настройка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/username/project-name.git
    cd project-name
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    .\venv\Scripts\activate   # Для Windows
    ```

3. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Скачайте и разместите вашу обученную модель YOLOv8 в указанной директории:

    ```plaintext
    C:\Users\SystemX\PycharmProjects\hak-pak-puk\config_file\best.pt
    ```

5. Запустите приложение:

    ```bash
    uvicorn main:app --reload
    ```

## Использование
Для отправки изображения на обработку используйте POST-запрос на эндпоинт `/process_image/` с JSON-объектом, содержащим изображение в формате Base64:

### Пример запроса:
```json
{
    "image_base64": "base64_строка_изображения"
}
Пример ответа:
json
Копировать код
{
    "text": "распознанный текст"
}
Структура проекта
plaintext
Копировать код
project-name/
│
├── main.py                  # Основной файл приложения
├── requirements.txt         # Список зависимостей проекта
├── README.md                # Описание проекта
└── config_file/
    └── best.pt              # Файл обученной модели YOLOv8
Зависимости
fuzzywuzzy
rapidfuzz
ultralytics
easyocr
opencv-python
fastapi
pydantic
Pillow
