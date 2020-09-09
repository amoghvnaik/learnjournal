FROM python:3.6.8
WORKDIR /learnjournal
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python manage.py migrate"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "learnjournal.wsgi:application"]
COPY . .
RUN python manage.py test

