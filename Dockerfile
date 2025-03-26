FROM ubuntu

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip python3-venv && \
    sudo rm -rf /var/lib/jenkins/workspace/futurelife/data-db/.mongodb

COPY requirements.txt /app/requirements.txt
COPY . /app


RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


