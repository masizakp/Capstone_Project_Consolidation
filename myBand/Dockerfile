# Use the official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project
COPY . /app/

# Apply migrations and run development server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
