
from click import command
from scrapli.driver.core import EOSDriver
from scrapli.driver.core import AsyncEOSDriver
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from ipaddress import ip_address , ip_network
import ipdb

target = input("Enter ip address = ")
ipadd = ip_address(target)

nr = InitNornir(config_file="config.yaml")

def get_routes(task):
    response = task.run(task=send_command, command="show ip route")
    task.host["facts"] = response.scrapli_response.genie_parse_output()
    prefixes = task.host["facts"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
    for prefix in prefixes:
        net = ip_network(prefix)
        if ipadd in net:
            print(f"{ipadd} is present on device {task.host} (network: {net} )")
        

nr.run(task=get_routes)

ipdb.set_trace()
