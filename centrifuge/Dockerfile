#Pull base image
FROM ubuntu:14.04

MAINTAINER Pedro J. Torres

#-------- Installing some basic essentials for Centrifuge-------------
RUN apt update && \
	apt-get install -y build-essential wget unzip  git awscli curl

# need python 2.7 for this to work
RUN  apt install -y  python-minimal
RUN  apt install -y  python-pip
# Download Centrifuge
RUN git clone https://github.com/infphilo/centrifuge \
&& mv centrifuge/centrifuge* /usr/bin

RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/downloads/centrifuge-1.0.3-beta-Linux_x86_64.zip \
&& unzip centrifuge-1.0.3-beta-Linux_x86_64.zip \
&& mv centrifuge-1.0.3-beta/centrifuge* /usr/bin

#-----------Execute ----
RUN chmod +x /usr/bin/*
