from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

nr = InitNornir(config_file="config.yaml")

def banner_config(task):
    task.run(netmiko_send_config, config_commands=["no banner motd #new banner#",
    "snmp-server community cisco","ntp server 1.1.1.1"])

result = nr.run(task=banner_config)
print_result(result)
