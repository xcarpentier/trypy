from PIL import Image

img1 = Image.open("pomme.jpg")
largeur, hauteur = img1.size
img2 = Image.new("RGB", (largeur, hauteur))
for y in range(hauteur):
    for x in range(largeur):
        r, g, b = img1.getpixel((x, y))
        pixel2 = (b, g, r)
        img2.putpixel((x, y), pixel2)
img2.save("pommener.jpg")
img2.show
