FROM python:3.8-slim

RUN apt-get update \
   && apt-get install gnupg1 apt-transport-https dirmngr -yq \
   && export INSTALL_KEY=379CE192D401AB61 \ 
   && export DEB_DISTRO=buster \
   && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY \
   && echo "deb https://ookla.bintray.com/debian ${DEB_DISTRO} main" | tee /etc/apt/sources.list.d/speedtest.list \
   && apt-get update \
   && apt-get install speedtest \
   && apt-get clean

RUN mkdir /opt/houseboat
WORKDIR /opt/houseboat

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src

WORKDIR /opt/houseboat/src
ENTRYPOINT ["python", "main.py"]
