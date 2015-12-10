#!/usr/bin/env python

import sys
import usb.core
import time


def detectSegger():
  
    # find Nordic Segger JLink
    try:
        dev = usb.core.find(idVendor=0x1366, idProduct=0x1015)
    except AttributeError: #Gets thrown if unplugged while iterating devices
        return False

    if dev is None:
            return False
    return True


if __name__ == "__main__":
    connected = detectSegger()
    wasConnected = connected
    while(True):
        connected = detectSegger()
        if connected != wasConnected:
            if connected:
                print ("Segger was plugged in")
            else:
                print ("Segger was unplugged")
        wasConnected = connected 
        time.sleep(1)


