from kubernetes import client, config
import datetime

try:
    config.load_kube_config()
except Exception as e:
    print(f'{datetime.datetime.now()}\nKube config file not found in /kube/config, starting anyway\n{e}')

v1 = client.CoreV1Api()
api = client.AppsV1Api()

def find_(namespace_, name_, t_kind):
    func = str('v1.list_namespaced_' + t_kind)
    try:
        ret = eval(func)(namespace=namespace_)
    except AttributeError:
        func = str('api.list_namespaced_' + t_kind)
        ret = eval(func)(namespace=namespace_)

    names = []
    for i in ret.items:
        if i.metadata.name.startswith(name_):
            names.append(i.metadata.name)
    
    return names

def delete_(namespace_, name_, t_kind):
    func = str('v1.delete_namespaced_' + t_kind)
    try:
        eval(func)(name=name_, namespace=namespace_)
    except AttributeError:
        func = str('api.delete_namespaced_' + t_kind)
        eval(func)(name=name_, namespace=namespace_)
