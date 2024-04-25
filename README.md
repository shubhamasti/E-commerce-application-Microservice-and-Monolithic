## Microservice E-commerece application
Python-flask application using mysql.

### Features
1. Login/Register page (authorization)
2. Product browsing
3. Cart page
4. Checkout page
5. View billing history

### Requirements
Docker and Kuberenetes

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
