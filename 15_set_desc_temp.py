
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command, netmiko_send_config

nr = InitNornir(config_file="config.yaml")

def cdp_map(task):
    r = task.run(task=netmiko_send_command, command_string="show cdp neighbor", use_genie=True)
    print(task.host)

results = nr.run(task=cdp_map)

