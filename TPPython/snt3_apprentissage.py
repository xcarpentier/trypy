# from PIL import Image
#
# img1 = Image.open("pomme.jpg")
# largeur, hauteur = img1.size
# img2 = Image.new("RGB", (largeur, hauteur))
# for y in range(hauteur):
#    for x in range(largeur):
#        r, v, b = img1.getpixel((x, y))
#        pixel2 = (
#            255 - r,
#            255 - v,
#            255 - b,
#        )
#        img2.putpixel((x, y), pixel2)
# img2.save("pomme_négatif.jpg")
# img2.show()

from math import sqrt
from PIL import Image

img1 = Image.open("pommecopie2.jpg")
largeur, hauteur = img1.size
img2 = Image.new("RGB", (largeur, hauteur))
seuil = 10
for y in range(1, hauteur - 1):
    for x in range(1, largeur - 1):
        r1, g1, b1 = img1.getpixel((x - 1, y))
        r2, g2, b2 = img1.getpixel((x, y - 1))
        r3, g3, b3 = img1.getpixel((x + 1, y))
        r4, g4, b4 = img1.getpixel((x, y + 1))
        I = sqrt((r1 - r2) ** 2 + (r2 - r4) ** 2)
        if I < seuil:
            pixel2 = (255, 255, 255)
        else:
            pixel2 = (0, 0, 0)
        img2.putpixel((x, y), pixel2)
img2.save("pommecontours.jpg")
# img2.show
