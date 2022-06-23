from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
target = input("Enter the mac address you want to find: ")

def pull_info(task):
    interface_result = task.run(task=send_command, command="show interfaces")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for interface in interfaces:
        mac_addr = interfaces[interface]["mac_address"]
        if target == mac_addr:
            intf = interface
            print_info(task, intf)

def print_info(task, intf):
    print(f"MAC Address: {target} is present on {task.host}'s {intf}")
    cdp_result = task.run(task=send_command, command="show cdp neighbors")
    task.host["cdpinfo"] = cdp_result.scrapli_response.genie_parse_output()
    index = task.host["cdpinfo"]["cdp"]["index"]
    for num in index:
        local_intf = index[num]["local_interface"]
        if local_intf == intf:
            dev_id = index[num]["device_id"]
            port_id = index[num]["port_id"]
            print(f"Connected to {dev_id} on its interface {port_id}")

nr.run(task=pull_info)
