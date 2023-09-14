FROM python:3.11-slim

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]


# FROM python:3.11-slim

# WORKDIR /app

# RUN pip install gunicorn==20.1.0

# COPY requirements.txt .

# RUN apt-get update && apt-get upgrade -y && \
#     pip install --upgrade pip && pip install -r requirements.txt

# COPY . .

# CMD ["gunicorn", "--bind", "0:8000", "backend.wsgi" ]






# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:9000", "kittygram_backend.wsgi"]


# FROM python:3.11

# WORKDIR /app

# RUN pip install gunicorn==20.1.0

# COPY requirements.txt .


# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# CMD ["python", "manage.py", "runserver", "0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]