FROM python:3.8-alpine
RUN apk update
RUN apk add build-base
ADD requirements.txt /game/
WORKDIR /game 
CMD ["pip3 install -r requirements.txt"]
