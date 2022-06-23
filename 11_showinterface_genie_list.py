from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command
from rich import print

nr = InitNornir(config_file="config.yaml")

def structured_test(task):
    r = task.run(task=netmiko_send_command,command_string="show ip interface", use_genie=True)
    task.host["facts"] = r.result
    lister = task.host['facts']['Ethernet0/3']['multicast_groups']
    for address in lister:
        if address == '224.0.0.10':
            print(f"{task.host}: [green]has OSPF enabled on its Ethernet0/3 interface[/green]")


results = nr.run(task=structured_test)
