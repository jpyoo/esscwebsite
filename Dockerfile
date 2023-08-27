FROM python:3.7.4-slim-buster as production
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app/

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements/prod.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

FROM production as development

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements/dev.txt

COPY . .