FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py
COPY models.py models.py

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]