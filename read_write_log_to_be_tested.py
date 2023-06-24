import serial
import time
from datetime import datetime

com_port = 'COM4'
baud_rate = 115200
command = bytearray([0x53, 0xAC, 0x00, 0x00, 0x01, 0x32, 0x11, 0x33, 0xAB, 0x05, 0x65, 0x98, 0x9A, 0x67, 0x8A, 0x55])
interval = 0.01  # 10 milliseconds
output_file = 'output.txt'

def write_command_to_comport(ser, command):
    ser.write(command)

def read_response_from_comport(ser):
    response = ser.read_all()
    return response

def main():
    with serial.Serial(com_port, baud_rate, timeout=1) as ser:
        with open(output_file, 'a') as file:
            while True:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                file.write(f'Timestamp: {timestamp}\n')
                file.write('Command: ' + ' '.join(hex(byte) for byte in command) + '\n')

                write_command_to_comport(ser, command)
                time.sleep(interval)

                response = read_response_from_comport(ser)
                file.write('Response: ' + ' '.join(hex(byte) for byte in response) + '\n\n')

                time.sleep(interval)

if __name__ == '__main__':
    main()
