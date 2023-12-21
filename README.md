Modbus Data Retrieval Script
This Python script is designed to continuously fetch data from a Modbus server using the pyModbusTCP library. It retrieves data based on specified addresses and data types and handles reconnection to the Modbus server in case of connection loss.

Requirements
Python 3.x
pyModbusTCP library (pip install pyModbusTCP)
Usage
Clone the repository or download the script modbus_data_retrieval.py.
Ensure you have the required Python version and install the dependencies.
Update addresses.json with the Modbus addresses and corresponding data types.
Run the script using the command: python modbus_data_retrieval.py.
Configuration
Modify the addresses.json file to include the Modbus addresses and their respective data types.
Adjust the IP address and port in the script (host="192.168.1.3", port=502) according to your Modbus server configuration.
Functionality
The script establishes a connection to the Modbus server and continuously reads data from specified Modbus addresses.
It handles reconnection attempts to the Modbus server in case of a lost connection.
If the connection fails, the script will attempt to reconnect and also check the LAN connection.
Important Note
Ensure that the Modbus server is reachable from the network where this script is executed.
Modify error handling or data processing according to your specific use case or requirements.
