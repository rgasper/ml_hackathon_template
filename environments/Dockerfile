FROM python:3.10-slim
# RUN adduser -D -g '' eis-user
RUN useradd -ms /bin/bash eis-user
ADD requirements.txt requirements.txt
RUN apt-get update && \
    apt-get -y install gcc
RUN pip install -r requirements.txt
USER eis-user
WORKDIR /home/eis-user