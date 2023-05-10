FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

EXPOSE 8000

ARG AP_UID=1000
ARG APP_GID=1000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    addgroup -g $APP_GID appgroup && \
    adduser -u $AP_UID -G appgroup -D app

ENV PATH="/py/bin:$PATH"

WORKDIR /app
COPY . /app
COPY /pre-start.sh /app/pre-start.sh
RUN chmod +x /app/pre-start.sh
RUN chown -R $AP_UID:$APP_GID /app

USER app

CMD ["sh", "/app/pre-start.sh"]
