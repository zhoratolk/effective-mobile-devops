FROM python:3.12-slim
WORKDIR /app
# Запуск от не-root пользователя для безопасности [cite: 74, 130]
RUN useradd -m myuser
USER myuser
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]