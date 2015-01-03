shadowColor = 0
midColor = 128
highColor = 255
def tritone(image):
	ar = list(image.getdata())
	new_ar = []

	lut = []
	for i in range(0, 128):
		t = i / 127.0
		lut.append(mixColors( t, shadowColor, midColor ))
    
	for i in range(0, 128):
		t = (i-127) / 128.0
		lut.append(mixColors( t, midColor, highColor ))
    
    

	for pixel in ar:
		Red = pixel[0]
		Green = pixel[1]
		Blue = pixel[2]

   		Gray = lut[(Red+ Green+ Blue)/3]
   		new_ar.append((Gray, Gray, Gray))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

def mixColors(t, rgb1, rgb2):
	r1 = rgb1
	r2 = rgb2
	g1 = rgb1
	g2 = rgb2
	b1 = rgb1
	b2 = rgb2

	r1 = lerp(t, r1, r2)
	g1 = lerp(t, g1, g2)
	b1 = lerp(t, b1, b2)

	return (r1+g1+b1)/3

def lerp(t, a, b):
	return int(a + t * (b - a))

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('aa.jpg')
	new = tritone(im)
	new.save('aa_tritone.jpg')
	