FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ необходимые файлы
COPY app.py service.py ./
# Если model.pkl должен быть внутри контейнера (а не через volume)
COPY model.pkl ./

EXPOSE 8501

# Это CMD по умолчанию, но docker-compose переопределит его
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]