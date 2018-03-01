FROM python:3.6

ADD . /ui-integration-tests

WORKDIR /ui-integration-tests

RUN pip install -r requirements.txt

RUN chmod +x wait-for-it.sh

ENTRYPOINT ["/bin/bash", "./wait-for-it.sh"]