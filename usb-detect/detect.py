#!/usr/bin/env python

import sys
import usb.core


def detectSegger():
  
    # find USB devices
    dev = usb.core.find(find_all=True)

    # loop through devices, printing vendor and product ids in decimal and hex
    for cfg in dev:
        if cfg.idVendor == 0x1366 and cfg.idProduct == 0x1015:
            return True
    return False


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



