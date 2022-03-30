FROM python:3

ADD maze.py /

RUN pip install pystrich

CMD [ "python", "./maze.py" ]