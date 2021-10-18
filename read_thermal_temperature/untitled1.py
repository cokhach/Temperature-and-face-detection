# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:17:27 2021

@author: nguyen tuan
"""
import json
import subprocess
cmd = "dir \n"
ps = subprocess.check_output(cmd,shell=True)
print(ps)
