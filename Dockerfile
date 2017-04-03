FROM python:2-alpine
MAINTAINER ACM@UIUC

# Get packages for native extensions
RUN apk add --update alpine-sdk libffi-dev openssl-dev

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app

EXPOSE 5652

CMD [ "python", "app.py" ]
