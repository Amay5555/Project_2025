FROM python:3.12
WORKDIR /my_app
COPY . /my_app
RUN pip install -r /my_app/requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
