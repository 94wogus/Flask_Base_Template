FROM python:3.6.10-alpine3.10

# Set the working directory
WORKDIR /Flask_Base_Teamplate

# Install pipenv
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN apk add --no-cache \
    libev libffi-dev\
    python3-dev build-base \
&& pip3 install gevent gunicorn \
&& apk del python3-dev build-base

RUN apk add --no-cache g++ gcc musl-dev make

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

# Make port 8000 available to the world outside this container
EXPOSE 8000

RUN chmod 555 boot.sh
# Run app.py when the container launches
ENTRYPOINT [ "./boot.sh" ]