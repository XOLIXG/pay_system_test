FROM python:3.10

WORKDIR /pay_api

COPY .requirements.txt /pay_api/requirements.txt

RUN pip3.10 install -r requirements.txt

COPY . /pay_api

CMD ["uvicorn", "fast:app","--reload", "-host=0.0.0.0"]