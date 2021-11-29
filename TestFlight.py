# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

# Square
def square():
    sendmsg("up 75")
    for i in range(4):
        sendmsg("forward 100")
        sendmsg("ccw 90")


# Triangle
def triangle():
    sendmsg("up 75")
    for i in range(3):
        sendmsg("forward 100",3)
        sendmsg("ccw 120",3)


print("\nWilliam Julian")
print("Project Name: Test Flight ")
import datetime

now = datetime.datetime.now()
print("Date: "+now.strftime("%m-%d-%y %H:%M"))
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yep':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        triangle()

        sendmsg('land')

        print('\nFLIGHT SUCCESSFUL!! :)')

    else:
        print('\n****ERROR****\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
