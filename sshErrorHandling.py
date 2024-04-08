from netmiko import ConnectHandler, exceptions
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from netmiko import exceptions

import logging
logging.basicConfig(filename = 'sshErrorHandling.log', level = logging.DEBUG)
logger = logging.getLogger("netmiko")

device_ips = ['192.168.20.2','192.168.20.3']

for device in device_ips:
	try:
		print(f"--------{device}--------")
		connection = ConnectHandler(host = device,
				 port= 22,
				 username='wrongUser',
				 password='baljot',
				 device_type='cisco_ios')
		print("Sucessfully connected...")
	except NetmikoAuthenticationException:
		print("Authentication Failed")
	except NetmikoTimeoutException:
		print(f"Session timeout")
