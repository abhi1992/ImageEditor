def threshold(image, T):
        ar = list(image.getdata())
        new_ar = []
        for pixel in ar:
            Red = pixel[0]
            Green = pixel[1]
            Blue = pixel[2]
            
            if((Red + Green + Blue)/3 > T):
                RGB = [255, 255, 255]
            else:
                RGB = [0, 0, 0]
            
            new_ar.append((RGB[0], RGB[1], RGB[2]))
        new_image = Image.new("RGB", image.size, "white")
        new_image.putdata(new_ar)
        return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('a.jpg')
	# new = color_adjust(im, invert)
	# new.save('color_adjust_invert.jpg')

	# new = color_adjust(im, solarize)
	# new.save('color_adjust_solarize.jpg')

	# new = color_adjust(im, posterize)
	# new.save('color_adjust_posterize.jpg')

	# new = glass(im)
	# new.save('aa_glass.jpg')
        
        
	new = threshold(im, 125)
	new.save('aaaa.jpg')
