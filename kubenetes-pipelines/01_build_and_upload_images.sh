cd Docker
docker build -t extract:v1 -f Dockerfile.extract .
docker build -t transform:v1 -f Dockerfile.transform .
docker build -t load:v1 -f Dockerfile.load .
# create the test cluster
k3d cluster create test-cluster
k3d image load extract:v1 -c test-cluster
k3d image load transform:v1 -c test-cluster
k3d image load load:v1 -c test-cluster