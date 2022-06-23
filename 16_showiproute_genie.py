from nornir import InitNornir

from nornir_utils.plugins.functions import print_result , print_title

from nornir_netmiko import netmiko_send_command, netmiko_send_config



nr = InitNornir(config_file="config.yaml")



def structured_test(task):

    task.run(netmiko_send_command, command_string="show ip route", use_textfsm=True)



results = nr.run(task=structured_test)

print_result(results)
