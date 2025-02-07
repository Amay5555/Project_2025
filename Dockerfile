FROM python:3.12
WORKDIR /myapp
COPY . /my_app
RUN pip install -r /my_app/requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
