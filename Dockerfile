FROM python:3.7.4-slim as production
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app/

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && pip install psycopg2

# Copy the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -q -r ./requirements/prod.txt

RUN pip install djangorestframework django-cors-headers

# Make port 8000 available to the world outside this container
EXPOSE 8000

FROM production as development

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -q -r ./requirements/dev.txt

COPY . .