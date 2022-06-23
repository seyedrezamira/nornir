from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def show_command(task):
    showver = task.run(netmiko_send_command, command_string="show version")
    #result = showver.result
    #print(result)

result = nr.run(task=show_command)
print_result(result)
