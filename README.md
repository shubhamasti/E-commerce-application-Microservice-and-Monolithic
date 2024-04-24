## Microservice E-commerece application

### How to run
Make sure to change mysql password

#### Pull docker images
docker compose up -d

#### Kuberenetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

##### Check status, wait till pods are ready
kubectl get deployments
kubectl get services
kubectl get pods

#### Run authservice to start application
minikube service authservice