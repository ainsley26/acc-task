echo "Building docker container with tag 'predictor'"
docker build --tag=predictor .
echo "Running docker container forwarding container port 80 to local port 5000"
docker run -p 5000:80 predictor
