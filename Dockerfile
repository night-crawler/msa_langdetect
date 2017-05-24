FROM python:3-alpine
RUN apk update && apk upgrade && pip install wheel && apk add enchant

RUN apk add mercurial \
    && hg clone https://bitbucket.org/spirit/guess_language /tmp/guess_language \
    && cd /tmp/guess_language && python ./setup.py install \
    && apk del mercurial

WORKDIR /application/msa_langdetect
ADD requirements.txt /application/msa_langdetect
RUN pip install -r requirements.txt

ADD . /application/msa_langdetect
RUN mkdir /application/log && mkdir /application/run

RUN adduser -D -u 1000 msa_langdetect -h /application
RUN chown -hR msa_langdetect: /application

USER msa_langdetect
EXPOSE 21021

ENTRYPOINT ["python", "manage.py"]
CMD ["gunicorn"]
