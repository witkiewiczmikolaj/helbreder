from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

def list_pods():
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

def kill_pod(namespace_, name_):
    v1.delete_namespaced_pod(name=name_, namespace=namespace_)