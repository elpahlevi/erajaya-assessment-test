FROM python:3.9.12-alpine

WORKDIR /flask-api

COPY requirements.txt requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Prevents Python writing out .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdin/stdout
ENV PYTHONBUFFERED=1

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]