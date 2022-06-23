
import json
from ttp import ttp
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command, netmiko_send_config




nr = InitNornir(config_file="config.yaml")

ttp_template="""
interface {{ intf }}
 ip address {{ ip }}  {{ mask }}
"""

def test(task):
    r = task.run(netmiko_send_command,command_string="show run int e0/0")
    datatoparse = r.result
    parser = ttp(data=datatoparse, template=ttp_template)
    parser.parse()
    json_result = json.loads(parser.result(format='json')[0])
    task.host["facts"] = json_result

results = nr.run(task=test)
import ipdb
ipdb.set_trace()
