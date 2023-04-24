mkdir -p /home/ayushsingh/jenkins
chmod 777 /home/ayushsingh/jenkins
docker build -t codercata5/jenkins .
docker run -d -p 8080:8080 -v /home/ayushsingh/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock  codercata5/jenkins