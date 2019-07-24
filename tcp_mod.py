
from pyModbusTCP.client import ModbusClient
#from pymodbus3.client.sync import ModbusTcpClient
#import pymodbus
#import ModbusTcpClient

try:
    client = ModbusClient(host="192.168.75.14", port=502, debug=True, unit_id=4)
    #client = ModbusClient(host="192.168.1.151", port=502, debug=True)
except ValueError:
    print("Error with host or port params")


if client.open():
	#client.write_single_coil(0,0)
	#client.write_multiple_coils(0,[1,1,1,1,1,1,1,1,1])
	#client.write_multiple_coils(0,[0,0,0,0,0,0,0,0,0])
	#client.write_multiple_registers(1001,[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
	#result = client.read_coils(102,8)
	#print (result)


	#client.write_single_register(0,15)
	#result = client.read_input_registers(10000,5)
	result = client.read_holding_registers(0,1)
	#result = client.read_discrete_inputs(2,1)
	#result = client.read_coils(0,8)
	#print (result)
	#result = client.read_discrete_inputs(0,8)
	print (result)
client.close()