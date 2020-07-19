FROM python:3.8-slim-buster

WORKDIR /api

COPY . .

RUN pip3 install -r requirements.txt

# RUN pytest -s

ENTRYPOINT [ "python3","-u", "run.py" ]
