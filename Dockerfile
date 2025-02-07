FROM python:3.12
WORKDIR /myapp
COPY . /my_app
RUN pip install -r /my_app/requirements.txt
RUN chmod -R 755 /myapp/test
EXPOSE 5000
CMD ["python", "main.py"]
