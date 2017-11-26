from random import randint
from PIL import Image
im=Image.open("abin.jpg")
pix=im.load()
print(im.size)
print(pix[10,10])
for i in range (500):
	for j in range (500):
		pix[i,j]=(randint(0,255),randint(0,255),randint(0,255))
im.save("abin2.jpg")


