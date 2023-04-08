FROM python:3

WORKDIR /projectMLops

COPY . /projectMLops

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main_.py"]

