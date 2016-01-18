#!/usr/bin/env python2

import sys
import subprocess
import usb.core
import time
import os.path
from jlink import jlink


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

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "/"
    wasConnected = detectSegger()
    while(True):
        connected = detectSegger()
        if connected != wasConnected:
            if connected:
                print ("Segger was plugged in")
                print ("Erasing...")
                subprocess.call(["nrfjprog", "--erase"])
                print ("Done. Programming softdevice...")
                subprocess.call(["nrfjprog", "--program", dirPath + "softdevice.hex"])
                print ("Done. Programming bootloader...")
                subprocess.call(["nrfjprog", "--program", dirPath + "bootloader.hex"])
                print ("Done. Reset.")
                subprocess.call(["nrfjprog", "--reset"])
            else:
                print ("Segger was unplugged")
                jl = None
        wasConnected = connected 
        time.sleep(1)


