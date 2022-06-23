
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result , print_title
from nornir_netmiko import netmiko_send_command, netmiko_send_config

nr = InitNornir(config_file="config.yaml")

def cdp_map(task):
    r = task.run(task=netmiko_send_command, command_string="show cdp neighbor", use_genie=True)
    task.host["facts"] = r.result
    indexer = task.host['facts']['cdp']['index']

    for idx in indexer:
        Local_intf = indexer[idx]['local_interface']
        Remote_intf = indexer[idx]['port_id']
        Remote_device = indexer[idx]['device_id']
        cdp_config = task.run(netmiko_send_config, name="Automating CDP Descriptions", config_commands=[
        f"interface {Local_intf}",
        f"descrip Connected to {Remote_device} via its {Remote_intf} interface"])

results = nr.run(task=cdp_map)
print_result(results)
