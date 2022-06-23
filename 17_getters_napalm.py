from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")
def ipvzero(task):
    task.run(task=napalm_get, getters=["get_interfaces"])

results = nr.run(task=ipvzero)
print_result(results)
import ipdb
ipdb.set_trace()

