#!/usr/bin/python3
from datetime import datetime
from fabric.api import env, run, local

env.hosts = ['54.165.117.227', '54.87.213.18']

def do_clean(number=0):
    """
    fabric_script to clean out all data of archive
    """
    if number < 0:
        print("Invalid Numbers, Please provide an integer number")
        return
