
from click import command
from scrapli.driver.core import EOSDriver
from scrapli.driver.core import AsyncEOSDriver

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")

def get_routes(task):
    response = task.run(task=send_command, command="show ip route")
    task.host["facts"] = response.scrapli_response.genie_parse_output()

nr.run(task=get_routes)

ipdb.set_trace()
