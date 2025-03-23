FROM ubuntu

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip python3-venv

COPY requirements.txt /app/requirements.txt
COPY ./futurelife /app/futurelife


RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app/futurelife
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


# # Use Python 3.9 as the base image
# FROM python:3.9

# # Set the working directory within the container
# WORKDIR /app/backend

# # Copy the requirements.txt file to the container
# COPY featurelife/requirements.txt /app/backend

# # Install Python dependencies using pip
# RUN pip install -r requirements.txt

# # Copy the entire application code to the container
# COPY . /app/backend

# # Expose port 8000 to the outside world
# EXPOSE 8000

# # Apply migrations to set up the database (SQLite in this case)
# RUN python manage.py migrate

# # Run the Django application
# CMD python /app/backend/FutureLife/featurelife/manage.py runserver 0.0.0.0:8000