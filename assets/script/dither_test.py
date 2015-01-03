threshold_map_4_4 = [[1, 9, 3, 11], 
					[13, 5, 15, 7],
					[4, 12, 2, 10],
					[16, 8, 14, 6]]

def _find_closest_palette_color(pixel):
	return int(pixel+0.5)

def ordered_dither(pixels):
	pass
	
def dither(image, mode=ordered_dither):
	pixel = image.load()
	# new_ar = []
	width, height = image.size
	new_image1 = image.copy()
	pixel = new_image1.load()
	fs_coeffs = [7.0,3.0,5.0,1.0]
	A,B,G,S = map(lambda x : float(x), fs_coeffs)
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			Red, Green, Blue = pixel[x, y]
			
	   		pix = float(Red + Green + Blue) / 3.0
	   		
	   		oldpixel = pix
			newpixel = _find_closest_palette_color(oldpixel)
			pixel[x, y] = (newpixel, newpixel, newpixel)
			quant_error = float(oldpixel - newpixel)

			import math
			
			if (x < image.size[0] - 1):
				print A;pixel[x+1,y] = (pixel[x+1,y][0] + int(math.ceil(A * quant_error)), pixel[x+1,y][1] + int(A * quant_error), pixel[x+1,y][2] + int(A * quant_error))
			if (x > 0) and (y < image.size[1] - 1):
			    pixel[x-1,y+1] = (pixel[x-1,y+1][0] + int(B * quant_error), pixel[x-1,y+1][1] + int(B * quant_error), pixel[x-1,y+1][2] + int(B * quant_error))
			if (y < image.size[1] - 1):
			    pixel[x,y+1] = (pixel[x,y+1][0] + int(G * quant_error), pixel[x,y+1][1] + int(G * quant_error), pixel[x,y+1][2] + int(G * quant_error))
			if (x < image.size[0] - 1) and (y < image.size[1] - 1):
			    pixel[x+1,y+1] = (pixel[x+1,y+1][0] + int(S * quant_error), pixel[x+1,y+1][1] + int(S * quant_error), pixel[x+1,y+1][2] + int(S * quant_error))
			
	      	# print pix
	      	# pixel[x,y] = (pix,pix,pix)
	# print i
	new_image1.save('a.jpg', 'jpeg')
	      	# new_image1.putpixel()
   	# print new_ar
   	# new_image = Image.new("RGB", image.size, "white")
   	# new_image.putdata(new_ar)
   	# return image


	

if __name__ == '__main__':
	from PIL import Image
	image = Image.open('grayscale_custom_shade.jpg')
	# dither(image)
	# new.save('dither_order.jpg')
	# import Image
 
	# img = Image.new( 'RGB', (255,255), "black") # create a new black image
	# pixels = im.load() # create the pixel map
	 
	# for i in range(im.size[0]):    # for every pixel:
	#     for j in range(im.size[1]):
	#         pixels[i,j] = (i, j, 0) # set the colour accordingly
	 
	# im.save('d.jpg')
	pixel = image.load()
	# new_ar = []
	width, height = image.size
	new_image1 = image.copy()
	pixel = new_image1.load()
	fs_coeffs = [7.0,3.0,5.0,1.0]
	A,B,G,S = map(lambda x : float(x)*16, fs_coeffs)
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			Red, Green, Blue = pixel[x, y]
			
	   		pix = float(Red + Green + Blue) / 3.0
	   		
	   		oldpixel = pix
			newpixel = _find_closest_palette_color(oldpixel)
			pixel[x, y] = (newpixel, newpixel, newpixel)
			quant_error = float(oldpixel - newpixel)

			import math
			
			if (x < image.size[0] - 1):
				pixel[x+1,y] = (pixel[x+1,y][0] + int(math.ceil(A * quant_error)), pixel[x+1,y][1] + int(A * quant_error), pixel[x+1,y][2] + int(A * quant_error))
			if (x > 0) and (y < image.size[1] - 1):
			    pixel[x-1,y+1] = (pixel[x-1,y+1][0] + int(B * quant_error), pixel[x-1,y+1][1] + int(B * quant_error), pixel[x-1,y+1][2] + int(B * quant_error))
			if (y < image.size[1] - 1):
			    pixel[x,y+1] = (pixel[x,y+1][0] + int(G * quant_error), pixel[x,y+1][1] + int(G * quant_error), pixel[x,y+1][2] + int(G * quant_error))
			if (x < image.size[0] - 1) and (y < image.size[1] - 1):
			    pixel[x+1,y+1] = (pixel[x+1,y+1][0] + int(S * quant_error), pixel[x+1,y+1][1] + int(S * quant_error), pixel[x+1,y+1][2] + int(S * quant_error))
			
	      	# print pix
	      	# pixel[x,y] = (pix,pix,pix)
	# print i
	new_image1.save('a.jpg', 'jpeg')