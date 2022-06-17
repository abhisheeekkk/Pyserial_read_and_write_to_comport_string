import time
import serial
import json
import sys
import logging
import threading
import schedule



ser = serial.Serial(
    port='/dev/ttyUSB1',\
    baudrate=2000000,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

# ser.isOpen()
# ser.flushInput()
# ser.flushOutput()

send = b'{"type":"perform","data":[{"msg":[{"_c":"66","_t":"1","_i":"3"}],"nodeId":492066213}]}\n'
# cor_on = json.dumps(send)
# cor_on[len(cor_on)] = NULL
# arg = bytes(cor_on,'utf-8')

def job():
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSShuklaSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    print(send)
    ser.write(send)
    # time.sleep(1)
    # ser.write(arg)
    # time.sleep(1)

# def read_serial():
#     data = ser.readline()
#     x=(data.decode('ISO-8859-1'))
#     # x= x.split("\n") 
#     print(x)

# while True:
#     read_serial()
# # t1 = threading.Thread(target=read_serial)
# # t2 = threading.Thread(target=job)

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()

# # threads = []

# # for _ in range(10):
# #     pass
# #     t = threading.Thread(target=read_serial)
# #     t.start()
# #     threads.append(t)
schedule.every(5).seconds.do(job)
print("connected to: " + ser.portstr)
# t1 = threading.Thread(target=job).start()
# time.start()

#this will store the line
seq = []
count = 1

while True:
    schedule.run_pending()
    for c in ser.read():
        seq.append(chr(c)) #convert from ANSII
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array

        if chr(c) == '\n':
            print("Line " + str(count) + ': ' + joined_seq)
            seq = []
            count += 1
            break
    # time.sleep(1)
        
    

ser.close()

