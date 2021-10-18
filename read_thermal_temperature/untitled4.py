# -*- coding: utf-8 -*-

import subprocess
import io
exiftool_path="exiftool"
flir_img_filename = 'FLIR_00001.tiff'
image_tag = "-ThumbnailImage"
visual_img_bytes = subprocess.check_output([exiftool_path, "-b", flir_img_filename], shell = True)
visual_img_stream = io.BytesIO(visual_img_bytes)
print(visual_img_bytes)

