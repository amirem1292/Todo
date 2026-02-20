FROM python:3.13.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
