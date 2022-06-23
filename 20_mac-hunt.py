from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")
target = input("Enter the mac address you want to find: ")

def pull_info(task):
    interface_result = task.run(task=send_command, command="show interfaces")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for interface in interfaces:
        mac_addr = interfaces[interface]["mac_address"]
        if target == mac_addr:
            print(f"{task.host}'s {interface} has the {mac_addr}")

nr.run(task=pull_info)
