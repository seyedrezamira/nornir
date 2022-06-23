from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command

import getpass

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password

def show_output(task):
    task.run(task=netmiko_send_command, command_string = "show ip interface brief")

results = nr.run(task = show_output)

print_title("Deploying Automation")
print_result(results)
