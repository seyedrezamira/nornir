from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command
from rich import print

nr = InitNornir(config_file="config.yaml")

def structured_test(task):
    r = task.run(task=netmiko_send_command,command_string="show version", use_genie=True)
    task.host["facts"] = r.result
    uptime = task.host['facts']['version']['uptime']

    print(f"the uptime of {task.host} is" +  uptime)


results = nr.run(task=structured_test)
