## Microservice E-commerece application

## How to run
Make sure to change mysql password


### Pull docker images
```bash
docker compose up -d
```


### Kuberenetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```


#### Check status, wait till pods are ready
```bash
kubectl get deployments
kubectl get services
kubectl get pods
```

#### Run authservice to start application
```bash
minikube service authservice
```
