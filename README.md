# SoftEng_text_model

## Sentiment Analysis API

Простое REST API для анализа тональности текста на разных языках с использованием [FastAPI](https://fastapi.tiangolo.com/) и предобученной модели из библиотеки [Hugging Face Transformers](https://huggingface.co/).

Модель: [`tabularisai/multilingual-sentiment-analysis`](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)  
Фреймворк: PyTorch

---

## 🚀 Возможности
- Принимает текст на нескольких языках.
- Определяет тональность текста: **положительная**, **отрицательная** или **нейтральная**.
- REST API с удобной документацией (Swagger UI и ReDoc автоматически доступны в FastAPI).

---

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```


2. Установите зависимости (рекомендуется использовать виртуальное окружение):

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Запуск

```bash
python main.py
```

или напрямую через uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

После запуска API будет доступно по адресу:
👉 [http://localhost:8000](http://localhost:8000)

---

## 📑 Примеры использования

### 1. POST `/predict`

Отправить текст для анализа тональности:

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "I love this project!"}'
```

Ответ:

```json
{
  "text": "I love this project!",
  "prediction": {
    "label": "positive",
    "score": 0.9987
  }
}
```

### 2. GET `/`

Проверка, что сервис работает:

```bash
curl http://localhost:8000/
```

Ответ:

```json
{"message":"Sentiment Analysis API"}
```

---

## 📖 Документация API

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠 Стек технологий

* Python 3.9+
* FastAPI
* Hugging Face Transformers
* PyTorch
* Uvicorn

---

## 📌 TODO

* [ ] Добавить Dockerfile для удобного деплоя
* [ ] Поддержка батчевой обработки текстов
* [ ] Логирование запросов в базу данных
