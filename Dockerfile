FROM python:3

WORKDIR /projectMLops

COPY . /projectMLops

# WORKDIR /app

# COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main_.py"]

