#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
import pandas

class Storage:

    def __init__(self):
        self.connectedDisks = None

    def getDisks(self):
        for i in psutil.disk_partitions():
            if "/dev/sda" in i.device:
                self.connectedDisks = i.device
                self.mountPoint = i.mountpoint

    def __repr__(self):
        return self.connectedDisks 

#[---------------MAIN-------------------]#
Blade = Storage()

Blade.getDisks()