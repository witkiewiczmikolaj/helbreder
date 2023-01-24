[![Helbreder docker image](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml/badge.svg?branch=main)](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml)

[Work in progress] 

# Helbreader - API for self-healing software

This is an REST API made for monitoring integration (webhooks mostly) in order to make self-healing operation simple.

## Deployment

It's an app made in Python 3 deployed as a docker image. It also uses basic HTML, CSS and Javascript. @wiktorkisielewski please provide some more info, thanks

## Demo

[helbreder.online](https://helbreder.online/)

Create an account by clicking the Sign up button and then click the link provided in an email sent to you to activate an account. You can then access your user panel where you can find some basic stats.

## Usage

#what can you do

### Generaing API calls

#how to use curlconverter

### Supported modules

#### k8s

The kubernetes module is based on [python kubernetes-client](https://github.com/kubernetes-client/python)

#### Standard fields

- `action`

- `namespace`

- `target_kind`

- `target_name`

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

#### Server

#### PSQL
