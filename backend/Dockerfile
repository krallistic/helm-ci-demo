FROM python:2.7

WORKDIR /backend

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD  __init__.py __init__.py
ADD server.py server.py
ADD tests/ tests/


EXPOSE 5000

CMD ["python", "server.py"]