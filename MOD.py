import time
import json
from pyModbusTCP.client import ModbusClient

client = ModbusClient(host="192.168.1.3", port=502)
value_address = 0  
holding_addresses = [2, 3, 4, 5, 6]
num_registers = 1

while True:
    if client.open():
        counter, overflow = client.read_holding_registers(value_address, 2)

        if counter and overflow:  
            actual_value = (overflow * 65535) + counter

            output_data = {
                "type": "actual_value",
                "timestamp": int(time.time()),
                "data": actual_value
            }

            json_output = json.dumps(output_data)
            print(json_output)

        for address in holding_addresses:
            data_holding = client.read_holding_registers(address, num_registers)

            if data_holding:
                output_data = {
                    "type": "holding",
                    "address": address,
                    "timestamp": int(time.time()),  
                    "data": data_holding[0] if len(data_holding) == 1 else data_holding
                }

                json_output = json.dumps(output_data)
                print(json_output)
    else:
        print("Connection ERROR")

    time.sleep(2)


# =============================================================================
# 
# {
#     "address": 4001,
#     "timestamp": "182937401",
#     "error_code": 1
# }
# =============================================================================
