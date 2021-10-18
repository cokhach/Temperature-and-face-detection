# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:48:51 2021

@author: nguyen tuan
"""
import subprocess
import json
exiftool_path="exiftool"
flir_img_filename = "p3027.bmp"
meta_json = subprocess.check_output([exiftool_path, "-RawThermalImageType", "-j", flir_img_filename], shell = True)
meta = json.loads(meta_json.decode())[0]
print(meta)


def get_image_type():
    """
    Get the embedded thermal image type, generally can be TIFF or PNG
    :return:
    """
    meta_json = subprocess.check_output([exiftool_path, "-RawThermalImageType", "-j", flir_img_filename], shell = True)
    meta = json.loads(meta_json.decode())[0]

    return meta['RawThermalImageType']

tt = get_image_type()
print(tt)