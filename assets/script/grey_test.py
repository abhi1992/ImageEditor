
def average(Red, Green, Blue):

   		return (Red + Green + Blue) / 3
   	
def luma(Red, Green, Blue):

   		return int (Red * 0.3 + Green * 0.59 + Blue * 0.11)

def desaturation(Red, Green, Blue):
	
	return ( max(Red, Green, Blue) + min(Red, Green, Blue) ) / 2
	
def max_decomposition(Red, Green, Blue):
	
	return max(Red, Green, Blue)

def min_decomposition(Red, Green, Blue):
	
	return min(Red, Green, Blue)

def red_channel(Red, Green, Blue):
	
	return Red

def green_channel(Red, Green, Blue):
	
	return Green

def blue_channel(Red, Green, Blue):
	
	return Blue
	
def custom_shade(Red, Green, Blue, number_of_shades=2):
	conversion_factor = 255 / (number_of_shades - 1)
	average_value = (Red + Green + Blue) / 3
	return int((average_value / conversion_factor) + 0.5) * conversion_factor

def grayscale(image, mode):
	ar = list(image.getdata())
	new_ar = []
	for pixel in ar:
		Red = pixel[0]
		Green = pixel[1]
		Blue = pixel[2]
                Gray = mode(Red, Green, Blue)
   		new_ar.append((Gray, Gray, Gray))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('b.jpg')
	
	new2 = grayscale(im, custom_shade)
	new2.save('new_b.jpg')
	
