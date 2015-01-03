from PIL import Image

def average(Red, Green, Blue, shades=0):

   		return (Red + Green + Blue) / 3
   	
def luma(Red, Green, Blue, shades=0):

   		return int (Red * 0.3 + Green * 0.59 + Blue * 0.11)

def desaturation(Red, Green, Blue, shades=0):
	
	return ( max(Red, Green, Blue) + min(Red, Green, Blue) ) / 2
	
def max_decomposition(Red, Green, Blue, shades=0):
	
	return max(Red, Green, Blue)

def min_decomposition(Red, Green, Blue, shades=0):
	
	return min(Red, Green, Blue)

def red_channel(Red, Green, Blue, shades=0):
	
	return Red

def green_channel(Red, Green, Blue, shades=0):
	
	return Green

def blue_channel(Red, Green, Blue, shades=0):
	
	return Blue
	
def custom_shade(Red, Green, Blue, number_of_shades=2):
	conversion_factor = 255 / (number_of_shades - 1)
	average_value = (Red + Green + Blue) / 3
	return int((average_value / conversion_factor) + 0.5) * conversion_factor

def invert(Red, Green, Blue, shades=0):
	return 255 - (Red + Green + Blue)/3

def grayscale(image, mode, shades=0):
	ar = list(image.getdata())
	new_ar = []
	for pixel in ar:
		Red = pixel[0]
		Green = pixel[1]
		Blue = pixel[2]

   		Gray = mode(Red, Green, Blue, shades)
   		new_ar.append((Gray, Gray, Gray))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('in.jpg')
	new = grayscale(im, invert)
	new.save('grayscale_invert.jpg')
	
	new2 = grayscale(im, luma)
	new2.save('grayscale_luma.jpg')
	
	new2 = grayscale(im, desaturation)
	new2.save('grayscale_desaturation.jpg')
	
	new2 = grayscale(im, max_decomposition)
	new2.save('grayscale_max_decomposition.jpg')
	
	new2 = grayscale(im, min_decomposition)
	new2.save('grayscale_min_decomposition.jpg')
	
	new2 = grayscale(im, red_channel)
	new2.save('grayscale_red.jpg')
	
	new2 = grayscale(im, green_channel)
	new2.save('grayscale_green.jpg')
	
	new2 = grayscale(im, blue_channel)
	new2.save('grayscale_blue.jpg')
	
	new2 = grayscale(im, custom_shade)
	new2.save('grayscale_custom_shade.jpg')
	