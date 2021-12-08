# from kubernetes import client, config
# from time import sleep
import psutil
import sched
import time

print("Hello World")

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    print(f'CPU :{cpu}')
    print(f'Memory :{mem}')
    s.enter(2, 1, do_something, (sc,))


s.enter(2, 1, do_something, (s,))
s.run()
#
# config.load_incluster_config()
# api = client.CustomObjectsApi()
#
# while True:
#     resource = api.list_namespaced_custom_object(group="metrics.k8s.io", version="v1beta1", namespace="default",
#                                                  plural="pods")
#     for pod in resource["items"]:
#         print(pod['containers'], "\n")
#     sleep(10)
