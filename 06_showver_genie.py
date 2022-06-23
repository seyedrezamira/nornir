from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def structured_test(task):
    r = task.run(task=netmiko_send_command,command_string="show version", use_genie=True)

results = nr.run(task=structured_test)
print_result(results)
