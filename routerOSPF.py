from netmiko import ConnectHandler

import logging
logging.basicConfig(filename = 'netmikoLogsOSPF.log', level = logging.DEBUG)
logger = logging.getLogger("netmiko")

device_ips = ['192.168.20.2','192.168.20.3']
ospf_config = ['router ospf 1', 'network 10.0.0.0 0.0.0.255 area 0']

for device in device_ips:
	print(f"--------{device}--------")
	connection = ConnectHandler(host = device,
			 port= 22,
			 username='baljot',
			 password='baljot',
			 device_type='cisco_ios',
			 secret='baljot')

	connection.enable()
	output = connection.send_config_set(ospf_config)
	print(output)
	print("Device configured...")
connection.disconnect()
