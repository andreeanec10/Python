#!/usr/bin/python3

import shutil
import psutil
from network import *

def check_disk_usage(disk):
    """Verify if the free space is more then 20%"""
    du = psutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

def check_cpu_usage():
    """Verify if the cpu usage is less than 75%"""
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") and not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything is OK!")
else:
    print("There is a connectivity problem")
