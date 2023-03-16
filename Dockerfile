#FROM registry.access.redhat.com/ubi8/python-38
FROM python:3.8-slim-buster
LABEL AUTHOR="Chandan Singh"
#RUN dnf update -y 
WORKDIR  /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY demoProject /app
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

