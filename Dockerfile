FROM python:3.9

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /var/logs

WORKDIR /var/www/
ENV PYTHONPATH=/var/www

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-c", "config/gunicorn.config.py", "app.server:app"]