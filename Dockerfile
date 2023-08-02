FROM python:3.10.3-slim

WORKDIR /app

COPY . .

CMD ["python", "args_seconds.py", "10"]
