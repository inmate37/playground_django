# Start with a base Python 3.10 image
FROM python:3.10

# Set an environment variable for the project name
ENV PROJECT_NAME myproject

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Set the default command for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
