from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")

def get_ip(task):
    response = task.run(task=send_command, command="show interface")
    task.host["facts"] = response.scrapli_response.genie_parse_output()

#nr.run(task=get_ip)
results = nr.run(task=get_ip)
print_result(results)
ipdb.set_trace()
