#/bin/bash

sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -f "dangling=true" -q)

sudo docker run -d --rm -p 80:80 --name web sami203/demo-docker:latest