#!/usr/bin/env python

import sys
import usb.core
import time
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
    _jl=None

    def jl():
        global _jl
        _jl = _jl or jlink.JLink()
        return _jl

    wasConnected = detectSegger()
    while(True):
        connected = detectSegger()
        if connected != wasConnected:
            if connected:
                print ("Segger was plugged in")
                print ("Erasing...")
                jl().halt()
                jl().erase_all()
                print ("Done. Programming softdevice...")
                jl().auto_program("softdevice.hex")
                jl().reset()
                print ("Done. Programming bootloader...")
                jl().auto_program("bootloader.hex")
                print ("Done. Reset.")
                jl().reset()
                jl().go()
            else:
                print ("Segger was unplugged")
        wasConnected = connected 
        time.sleep(1)


