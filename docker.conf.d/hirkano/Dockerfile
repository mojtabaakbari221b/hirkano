FROM python:3.9

LABEL MAINTAINER="hirkano | https://hirkano.com"
LABEL VERSION="1.0a"

ENV PYTHONUNBUFFERED 1
ENV HOME=/opt/hirkano/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
ADD requirements.txt $HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY configs $HOME/configs
COPY manage.py $HOME
COPY hirkano $HOME/hirkano

COPY docker.conf.d/hirkano/entrypoint.sh $HOME

ENTRYPOINT ["sh", "./entrypoint.sh"]