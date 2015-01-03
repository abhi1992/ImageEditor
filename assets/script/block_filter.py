blockSize = 200
pix = []
new_ar = []
import math
def getRGB(x, y, w, h, ar):
	global pix
	# pix = []

	for i in range(0, h):
		for j in range(0, w):
			pix.append(ar[i*w + j-1])

def setRGB(x, y, w, h, rgb):
	global new_ar
	for i in range(x, w):
		for j in range(y, h):
			new_ar[j*w + i-1] = 0


def block(image):
	ar = list(image.getdata())
	global new_ar, pix
	
	for i in range(len(ar)):
		new_ar.append([ar[i][0], ar[i][1], ar[i][2]])

	width, height = image.size
	for y in range(0, height, blockSize):
		for x in range(0, width, blockSize):
			w = min( blockSize, width-x )
			h = min( blockSize, height-y )
			t = w*h
			getRGB(x, y, w, h, ar)
			# print pix
			r = 0
			g = 0
			b = 0

			i = 0
			for by in range(0, h):
				for bx in range(0, w):
					argb = pix[i]
                	r += argb[0]
                	g += argb[1]
                	b += argb[2]
                	i += 1
			print r,g,b
			r = int(r/t)
			g = int(g/t)
			b = int(b/t)
			for i in range(x, w):
				for j in range(y, h):
					# print new_ar[j*w + i-1][0], r

					new_ar[j*w + i-1][0] = r
					new_ar[j*w + i-1][1] = g
					new_ar[j*w + i-1][2] = b
	k = []
	# print new_ar
	for i in range(len(ar)):
		k.append((new_ar[i][0], new_ar[i][1], new_ar[i][2]))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(k)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('a.jpg')
	new = block(im)
	new.save('a_block.jpg')