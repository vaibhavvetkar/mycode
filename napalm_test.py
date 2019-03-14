from napalam import get_network_driver
import pprint

driver = get_network_driver('eos')
device = driver('172.16.2.10', 'admin' , 'alta3')


