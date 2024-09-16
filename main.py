from pyModbusTCP.client import ModbusClient
from dotenv import load_dotenv
import os


load_dotenv() 


if __name__ == '__main__':
    try:
        ip = os.getenv('IP')
        port = int(os.getenv('PORT'))
        id = int(os.getenv('ID'))
        
        c = ModbusClient(host=ip, port=port, unit_id=id, auto_open=True)
        
        while True:
            address = int(input('[?] Address: '))
            size = int(input('[?] Size: '))
            regs = c.read_holding_registers(address, size)
            
            if regs:
                print(f'[+] Read: {regs}')
            else:
                print("[-] Read error")
    except Exception as ex:
        print(f'[-] {ex}')