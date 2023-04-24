docker build -t myjenkins-image .
docker run --name myjenkins-container -p 8080:8080 -p 50000:50000 -v /var/jenkins_home myjenkins-image
