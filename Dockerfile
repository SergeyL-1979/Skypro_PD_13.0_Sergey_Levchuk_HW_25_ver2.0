# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9.5-slim

# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /backend

# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /backend
RUN pip install --upgrade pip -r requirements.txt

# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, в рабочую директорию контейнера
COPY . /backend

# Устанавливаем порт, который будет использоваться для сервера
CMD flask run -h 0.0.0.0 -p 5000