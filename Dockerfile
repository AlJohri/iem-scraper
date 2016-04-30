FROM python:3.5

RUN apt-get update && apt-get install -y python-pip

ADD requirements.txt /code/

RUN pip install -r /code/requirements.txt

ADD . /code

WORKDIR /code

EXPOSE 5000

CMD ["python", "/code/web.py"]
