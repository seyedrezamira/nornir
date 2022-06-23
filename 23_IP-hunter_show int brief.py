from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")
my_list = []

def get_ip(task):
    response = task.run(task=send_command, command="show ip interface brief")
    task.host["facts"] = response.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for intf in interfaces:
        ip_key = interfaces[intf]
        for num_int in ip_key:
            phy_add = ip_key[num_int]["ip_address"]
            my_list.append(phy_add)
            print(f"The interface of {num_int} on {task.host} has {phy_add} address")
            
                   
nr.run(task=get_ip)
print(my_list)