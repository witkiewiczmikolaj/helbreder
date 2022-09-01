[Work in progress] [![Helbreder docker image](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml/badge.svg?branch=main)](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml)

# Helbreader - API for self-healing software

This is an REST API made for monitoring integration (webhooks mostly) in order to make self-healing operation simple

[Docker image](https://hub.docker.com/repository/docker/wiktorkisielewski/helbreder)

## How to run

### Authorization



### Production grade



### Local / test enivronment (docker)

`docker run -dt -p 80:5000 wiktorkisielewski/helbreder`

for k8s connection add: 

> `-v ~/.kube/config:/kube/config --env KUBECONFIG=/kube/config `

### Kubernetes

## Example requests

### Kubernetes 

- Kill a pod with specified name and namespace

    > json data

    ```json
    {
    "namespace": "$NAMESPACE", 
    "action": "$ACTION", 
    "target_name": "$NAME", 
    "target_kind": "$KIND"
    }
    ```

    > target endpoint: `http://$HELBREDER_URL:80/api/k8s`
