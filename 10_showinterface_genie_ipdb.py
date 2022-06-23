from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def structured_test(task):
    r = task.run(task=netmiko_send_command,command_string="show ip interface", use_genie=True)
    task.host["facts"] = r.result

results = nr.run(task=structured_test)
print_result(results)

import ipdb
ipdb.set_trace()
