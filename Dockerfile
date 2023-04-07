FROM python:3

WORKDIR /var/lib/docker/tmp/buildkit-mount3857901467/Dockerfile

# COPY . /projectMLops

# WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main_.py"]

