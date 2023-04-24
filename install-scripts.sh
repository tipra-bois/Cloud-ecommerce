docker build -t codercata5/jenkins .
docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock codercata5/jenkins