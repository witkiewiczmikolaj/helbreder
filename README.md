[![Helbreder docker image](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml/badge.svg?branch=main)](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml)

[Work in progress] 

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

## Modules

### Kubernetes 

The kubernetes module is based on [python kubernetes-client](https://github.com/kubernetes-client/python)

#### Standard fields

- `action` &#8594; [supported actions](#supported-actions)

- `namespace` &#8594; [k8s docs](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

- `target_kind` &#8594; `pod | deployment | stateful_set`

- `target_name` &#8594; name of the target

> Wildcard can be used at the end of the name
>
>`some_name*` - will match any object/s with name starting with "some_name"

#### Supported actions

- `delete` - removes an object from cluster, based on its name and declared namespace

#### Example

- Delete a pod with specified name and namespace

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
