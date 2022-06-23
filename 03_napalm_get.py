from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")

def get_config(task):
    task.run(task=napalm_get, getters=["get_facts"])

result = nr.run(task=get_config)
print_result(result)
