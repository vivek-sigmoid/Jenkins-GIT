from kubernetes import client, config
from time import sleep

config.load_incluster_config()
api = client.CustomObjectsApi()

print("Hello World")
while True:
    resource = api.list_namespaced_custom_object(group="metrics.k8s.io", version="v1beta1", namespace="default",
                                                 plural="pods")
    for pod in resource["items"]:
        print(pod['containers'], "\n")
    sleep(10)
