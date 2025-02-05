FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
# ENV TZ=UTC

RUN apt-get -y update

RUN apt-get install -y --no-install-recommends tzdata
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# RUN apt-get install -y --no-install-recommends python3.12
# RUN apt-get install -y --no-install-recommends python3-pip
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
#ENV PYTHONUNBUFFERED=1 

COPY ./requirements.txt /app

# RUN python3 -m pip install --no-cache-dir --upgrade --break-system-packages -r requirements.txt
RUN python3 -m pip install --no-cache-dir --break-system-packages -r requirements.txt

CMD ["/bin/bash"]
