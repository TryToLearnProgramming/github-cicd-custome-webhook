if [ ! -x "$(command -v docker)" ]
then
    sudo apt install -y docker.io
fi

if [ $(sudo docker ps -aq)!="" ]
then
    echo "removing old cotainer and Image...\n"
    sudo docker rm -f $(sudo docker ps -aq)
    sudo docker rmi -f $(sudo docker images -aq)
fi

echo "Running new image..."
sudo docker run -d --rm -p 80:80 --name web sami203/demo-docker:$1