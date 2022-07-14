FROM python:3.9.2

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

ENV PORT 8000
ENV HOST "0.0.0.0"
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install psycopg2 
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD ["uvicorn","main:app","--host", "0.0.0.0", "--port", "8000","--reload"]
