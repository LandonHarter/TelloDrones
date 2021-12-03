# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 8889
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address

# Creates a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1024)
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

def firstHoop():
    sendmsg('up 55')
    sendmsg('forward 185')

def secondHoop():
    sendmsg('go 175 0 35 65', 8)

def thirdHoop():
    sendmsg('curve 100 100 0 30 250 0 60', 10)
    sendmsg('ccw 180')
    sendmsg('forward 150')

def fourthHoop():
    sendmsg('go 175 0 -45 65', 8)

print("\nTeam: Harter & Julian")
print("Program Name: Hoop Competition")
import datetime

now = datetime.datetime.now()
print("Date: "+now.strftime("%m-%d-%y %H:%M"))
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff', 8)
        sendmsg('mon')
        sendmsg('mdirection 0')
        sendmsg('go 180 0 55 65 mid2')

        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program

        #firstHoop()
        #secondHoop()
        #thirdHoop()
        #fourthHoop()

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()