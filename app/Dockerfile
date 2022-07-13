FROM python:3.9.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install psycopg2 
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
RUN pip install gunicorn


EXPOSE 8000/tcp

CMD ["gunicorn","-k","uvicorn.workers.UvicornWorker","app.main:app"]
