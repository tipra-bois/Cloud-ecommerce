cd users-docker
docker build . --tag users-docker


cd ..
cd orders-docker
docker build . --tag orders-docker

cd ..
cd products-docker
docker build . --tag products-docker

cd ..

export MONGODB_VERSION=6.0-ubi8
docker run --name mongodb -d -p 27017:27017 -v $(pwd)/data:/data/db  --network mongodb  mongodb/mongodb-community-server:$MONGODB_VERSION

