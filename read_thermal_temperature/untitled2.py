# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:24:57 2021

@author: nguyen tuan
"""

import subprocess
ps = subprocess.Popen("ls",shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print(output)