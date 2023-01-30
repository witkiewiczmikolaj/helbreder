# Helbreader - API for self-healing software

This is a flask application that supports REST API requests and is able to create them.

[![Helbreder docker image](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml/badge.svg?branch=main)](https://github.com/wiktorkisielewski/helbreder/actions/workflows/image_builder.yml)

[Version Alpha 0.8.1]

## Deployment

It's an app made in Python 3 deployed as a docker image. It also uses basic HTML, CSS and Javascript. @wiktorkisielewski please provide some more info, thanks

## Demo

[helbreder.online](https://helbreder.online/)

#### Creating an account

Create an account by clicking the Sign up button and then click the link provided in an email sent to you to activate an account. You can then access your user panel where you can find some basic stats and you can generate the CPU usage graph of your server.

## Usage

With Helbreder you can create a code for sending API requests for modules in many different programming languages.

### Generating API calls

First you need to choose a `module`. Then you can choose an `action` and `target kind` associated with choosen module. If necessary you can also add some `additional info`. Then you only have type in `username` and `password` for authentication. When done click on `Submit` and you are ready to see the results. Just click on any icon of choosen language and you should be able to see the request. You can easily copy the code by clicking copy icon below the code. You can also toggle night mode by clicking an icon in top left corner.

### Supported modules

#### k8s

The kubernetes module is based on [python kubernetes-client](https://github.com/kubernetes-client/python)

#### Standard fields for k8s

- `action` &#8594; `Delete`

- `namespace`

- `target_kind` &#8594; `Pod | Deployment | Statefull_Set`

- `target_name` &#8594; name of the target

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

    > target endpoint: `http://helbreder.online/api/kubernetes`

#### Server

@wiktorkisielewski please add some info

#### Standard fields for Server

- `action` &#8594; `Reboot | Get_stats`

- `target_kind` &#8594; `Cpu | Ram | Memory_Main | None`

- `target_name` &#8594; `User | IP | Resource Type`

target endpoint: `http://helbreder.online/api/server`

#### PSQL

@wiktorkisielewski please add some info

#### Standard fields for PSQL

- `action` &#8594; `Drop`

- `target_kind` &#8594; `Database | Connection`

- `target_name` &#8594; name of the target

target endpoint: `http://helbreder.online/api/postgresql`
