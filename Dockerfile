# Take image with python
FROM python:2.7-slim

# Set working directory to /app
WORKDIR /app

# Copy current directory to /app
ADD . /app

# Install requirements
RUN pip install -r requirements.txt

# Open port 80
EXPOSE 80

CMD ["python", "manage.py", "runserver"]
