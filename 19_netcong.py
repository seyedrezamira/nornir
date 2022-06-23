from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
#from nornir_netmiko import netconf_get_config
#from nornir_netconf.plugins.tasks import netconf_get_config
from xml.dom import minidom


nr = InitNornir(config_file="config.yaml")

def getter(task):
    result = task.run(task=netconf_get_config, source="running").result
    result_pretty = minidom.parseString(result).toprettyxml()
    print(result_pretty)

outcome = nr.run(task=getter)
print_result(coutcome)

