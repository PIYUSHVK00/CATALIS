import time
import json
from pyModbusTCP.client import ModbusClient


client = ModbusClient(host="192.168.1.1", port=502)
addresses = [(0, 1), (2, 0), (3, 1), (5, 0), (6, 0), (7, 0), (8, 1)]


def read_data(address, data_type):
    if data_type == 1:  
        data = client.read_holding_registers(address, 2)
        if data:
            counter, overflow = data
            double = (overflow * 65536) + counter
            return double
    elif data_type == 0:  
        data = client.read_holding_registers(address, 1)
        if data:
            return data[0]
    return None


connected = client.open()

while True:    
    if not connected:
        print("CHECK LAN")
        connected = client.open()
        time.sleep(2)
        continue

    output_data = []
    for addr, data_type in addresses:
        result = read_data(addr, data_type)
        if result:
            output_data.append({
                "type": "double" if data_type == 1 else "holding",
                "address": addr,
                "timestamp": int(time.time()),
                "data": result
            })

    for data_point in output_data:
        json_output = json.dumps(data_point)
        print(json_output)

    time.sleep(2)
