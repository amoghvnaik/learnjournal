FROM python:3.6.8
WORKDIR /learnjournal
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "learnjournal.wsgi:application"]
COPY . .
ENV NAME=${NAME}
ENV TEST_NAME=${TEST_NAME}
ENV USER=${USER}
ENV PASSWORD=${PASSWORD}
ENV HOST=${HOST}
ENV SECRET_KEY=${SECRET_KEY}
