from kubernetes import client, config
import datetime

try:
    config.load_kube_config()
except Exception as e:
    print(f'{datetime.datetime.now()}\nKube config file not found in /kube/config, starting anyway\n{e}')

v1 = client.CoreV1Api()
api = client.AppsV1Api()

def pod_find(namespace_, name_):
    ret = v1.list_namespaced_pod(namespace_)
    for i in ret.items:
        if name_ in i.metadata.name:
            return i.metadata.name

def delete_(namespace_, name_, t_kind):
    try:
        func = str('v1.delete_namespaced_' + t_kind)
        eval(func)(name=name_, namespace=namespace_)
    except AttributeError:
        func = str('api.delete_namespaced_' + t_kind)
        eval(func)(name=name_, namespace=namespace_)
