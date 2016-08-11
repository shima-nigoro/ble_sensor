#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2016, shima-nigoro
# This software is under the terms of Apache License v2 or later.

from __future__ import print_function

import sys
import time
from gattlib import GATTRequester
from gattlib import DiscoveryService

class SensorTag(object):
    def __init__(self, address):
        self.requester = GATTRequester(address, False)

    def connect(self):
        print("Connecting...")
        self.requester.connect(True)
        print("Succeed.")

    def check_status(self):
        status = "connected" if self.requester.is_connected() else "not connected"
        print("Checking current status: {}".format(status))

    def disconnect(self):
        print("Disconnecting...")
        self.requester.disconnect()
        print("Succeed.")

    def show_primary(self):
        print("Discover Primary...")
        primary = self.requester.discover_primary()
        for prim in primary:
            print(prim)
        print("Done.")

    def show_characteristic(self):
        print("Discover Characteristic...")
        characteristic = self.requester.discover_characteristics()
        for char in characteristic:
            print(char)
        print("Done.")

class DiscoverDevice():
    def GetDeviceList(self):
        service = DiscoveryService("hci0")
        device = service.discover(2)
        return device

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        sys.exit(1)

    tag = SensorTag(sys.argv[1])
    tag.connect()
    tag.show_primary()
    tag.disconnect()
    print("Done.")