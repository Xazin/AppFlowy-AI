# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

# Define environment variable
ARG FLASK_DEBUG="false"
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_APP="hello.app" \
    FLASK_SKIP_DOTENV="true" \
    PYTHONUNBUFFERED="true"

CMD ["gunicorn", "-c", "python:config.gunicorn", "app:create_app()"]
