# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:35:21 2021

@author: nguyen tuan
"""

import subprocess
ps = subprocess.Popen("dir \n",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print(output)