from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config , netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def config_demo(task):
    task.run(task=netmiko_send_config, config_file= "configuration_file.txt")
    task.run(netmiko_send_command, command_string="show run")

result = nr.run(task=config_demo)
print_result(result)
