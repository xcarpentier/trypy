# -*- coding: utf-8 -*-
# PIL est une bibliothèque qui permet de traiter les images
import PIL.Image

img = PIL.Image.open("Pavlova.jpeg")
exif_data = img.getexif()
print(exif_data)
