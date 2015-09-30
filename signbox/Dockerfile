FROM debian:jessie
MAINTAINER Jean-Christophe Sirot <jcsirot@chelonix.com>

RUN apt-get update -qq && apt-get install -yqq curl

# Install java
RUN curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u60-b27/server-jre-8u60-linux-x64.tar.gz | tar xfz - -C /

ENV JAVA_HOME /jdk1.8.0_60
ENV PATH $PATH:$JAVA_HOME/bin

WORKDIR /signbox

ADD target/signbox.jar /signbox/signbox.jar

EXPOSE 9090
ENTRYPOINT ["java", "-DPROD_MODE=true", "-Xmx2G", "-jar", "signbox.jar"]