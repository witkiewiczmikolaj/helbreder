from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

def pod_find(namespace_, name_):
    ret = v1.list_namespaced_pod(namespace_)
    for i in ret.items:
        if name_ in i.metadata.name:
            return i.metadata.name

def kill_pod(namespace_, name_):
    v1.delete_namespaced_pod(name=name_, namespace=namespace_)