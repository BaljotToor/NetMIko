from netmiko import ConnectHandler

device_ips = ['192.168.20.2','192.168.20.3']

config_router1 = ['int f0/0', 'ip address 10.0.0.1 255.255.255.252', 'no shutdown']
config_router2 = ['int f0/0', 'ip address 10.0.0.2 255.255.255.252', 'no shutdown']

for device in device_ips:
	print(f"--------{device}--------")
	connection = ConnectHandler(host = device,
			 port= 22,
			 username='baljot',
			 password='baljot',
			 device_type='cisco_ios',
			 secret='baljot')
	connection.enable()

	if device == '192.168.20.2':
		output = connection.send_config_set(config_router1)
		print(output)
	elif device == '192.168.20.3':
		output = connection.send_config_set(config_router2)
		print(output)
connection.disconnect()
