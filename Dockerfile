# syntax=docker/dockerfile:1

# Use a lightweight Python base image
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim-buster

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /chatbot_app/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production


# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]