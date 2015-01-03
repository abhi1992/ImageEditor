def posterize(Red, Green, Blue, number_of_shades=4):
	conversion_factor = 255 / (number_of_shades - 1)
	
	nR = int((Red / conversion_factor) + 0.5) * conversion_factor
	nG = int((Green / conversion_factor) + 0.5) * conversion_factor
	nB = int((Blue / conversion_factor) + 0.5) * conversion_factor

	return [nR, nG, nB]

def invert(Red, Green, Blue):
	return [255 - (Red), 255-Green, 255-Blue]


        

def solarize(Red, Green, Blue, Threshold=10):

	nR = Red
	nG = Green
	nB = Blue

	if(Red > Threshold):
		nR = 255 - nR
	if(Green > Threshold):
		nG = 255 - nG
	if(Blue > Threshold):
		nB = 255 - nB

	return [nR, nG, nB]


def channel_mix(r, g, b):
	'''
	'''
	intoR = 0
	intoG = 0
	intoB = 255

	blueGreen = 0
	redBlue = 0
	greenRed = 255

	nR = (int) (intoR * (blueGreen*g+(255-blueGreen)*b)/255 + (255-intoR)*r)/255
	nG = (int) (intoG * (redBlue*b+(255-redBlue)*r)/255 + (255-intoG)*g)/255
	nB = (int) (intoB * (greenRed*r+(255-greenRed)*g)/255 + (255-intoB)*b)/255

	return [nR, nG, nB]

def color_adjust(image, mode):
        from PIL import Image
	ar = list(image.getdata())
	new_ar = []
	for pixel in ar:
		Red = pixel[0]
		Green = pixel[1]
		Blue = pixel[2]
                
   		RGB = mode(Red, Green, Blue)
   		new_ar.append((RGB[0], RGB[1], RGB[2]))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

def glass(image):
	import random
	ar = list(image.getdata())
	new_ar = []
	for i in range(0, len(ar)):

		r = random.randint(i, i+50)

		if(r > len(ar)):
			r = random.randint(i-50, i)
		if(r < 0):
			r = 0
		if(r > len(ar)):
			r = len(ar)-1
   		new_ar.append((ar[r][0], ar[r][1], ar[r][2]))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('in.jpg')
	# new = color_adjust(im, invert)
	# new.save('color_adjust_invert.jpg')

	# new = color_adjust(im, solarize)
	# new.save('color_adjust_solarize.jpg')

	# new = color_adjust(im, posterize)
	# new.save('color_adjust_posterize.jpg')

	# new = glass(im)
	# new.save('aa_glass.jpg')
        
        
	# new = color_adjust(im, channel_mix)
	# new.save('channel_mix.jpg')

