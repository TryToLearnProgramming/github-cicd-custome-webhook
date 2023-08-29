#/bin/bash

if [ "$1" == "on" ]; then

 

# Remove dangling container
docker rmi $(docker images -f "dangling=true" -q)

echo "Deploying app with docker"
docker-compose up --build -d



elif [ "$1" == "off" ]; then

echo "Stopping docker deployment"
docker-compose down