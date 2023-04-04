FROM python:3

WORKDIR /projectMLops
COPY . /projectMLops
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gradio", "main_"] 
