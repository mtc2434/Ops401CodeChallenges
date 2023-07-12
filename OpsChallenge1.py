#!/usr/bin/env python3
# Script:  OpsChallenge1.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/12/2023  
import os
import time
import datetime

def ping(host):
    #pings host once
    response = os.system("ping -c 1 " + host)  
    #The output is true if it is equal to 0
    return response == 0  
