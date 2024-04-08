from netmiko import ConnectHandler

device_ips = ['192.168.20.2','192.168.20.3']

for device in device_ips:
	print(f"--------{device}--------")
	connection = ConnectHandler(host = device,
			 port= 22,
			 username='baljot',
			 password='baljot',
			 device_type='cisco_ios')

	output = connection.send_command('show ip interface brief')
	print(output)

connection.disconnect()
