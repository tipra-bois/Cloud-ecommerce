FROM jenkins/jenkins
USER root
RUN if [ ! -d "/var/jenkins_home" ]; then mkdir /var/jenkins_home && chown -R jenkins:jenkins /var/jenkins_home; fi

RUN chown -R jenkins:jenkins /var/jenkins_home
RUN apt-get update && \
    apt-get install -y docker.io && \
    usermod -aG docker jenkins

VOLUME /var/jenkins_home
EXPOSE 8080
EXPOSE 50000
USER jenkins
