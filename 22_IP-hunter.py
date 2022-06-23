from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_ip(task):
    response = task.run(task=send_command, command="show interfaces")
    task.host["facts"] = response.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for intf in interfaces:
        ip_key = interfaces[intf]["ipv4"]
        for ip in ip_key:
              ip_addr = ip_key[ip]["ip"]
              print(ip_addr)
       
nr.run(task=get_ip)

