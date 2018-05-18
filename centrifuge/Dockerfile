#Pull base image
FROM ubuntu:14.04

MAINTAINER Pedro J. Torres

#-------- Installing wget to be able to download the DIAMOND sequence aligner -------------
RUN apt update && \
	apt-get install -y build-essential wget unzip  git awscli curl
  
# Download Centrifuge
RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/downloads/centrifuge-1.0.3-beta-Linux_x86_64.zip \
&& unzip centrifuge-1.0.3-beta-Linux_x86_64.zip \
&& mv centrifuge-1.0.3-beta/centrifuge* /usr/bin

#-----------Execute ----
RUN chmod +x /usr/bin/*
