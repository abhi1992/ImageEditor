_range = 3
levels = 256

def oil(image):

	''''''

	ar = list(image.getdata())
	width, height = image.size
	new_ar = []
	rHistogram = []
	gHistogram = []
	bHistogram = []
	rTotal = []
	gTotal = []
	bTotal = []
	index = 0

	for y in range(0, height):
		for x in range(0, width):
			for i in range(0, levels):
				rHistogram.append(0)
				gHistogram.append(0)
				bHistogram.append(0)
				rTotal.append(0)
				gTotal.append(0)
				bTotal.append(0)

			for row in range(-_range, _range+1):
					iy = y+row
					
					if (0 <= iy and iy < height):
						ioffset = iy*width
						for col in range(-_range, _range+1):
							ix = x+col;
							if (0 <= ix and ix < width):
								rgb = ar[ioffset+ix]
								r = rgb[0]
								g = rgb[1]
								b = rgb[2]
								ri = r*levels/256
								gi = g*levels/256
								bi = b*levels/256
								rTotal[ri] += r
								gTotal[gi] += g
								bTotal[bi] += b
								rHistogram[ri]+=1
								gHistogram[gi]+=1
								bHistogram[bi]+=1

			r = 0
			g = 0 
			b = 0
			for i in range(1, levels):
				if (rHistogram[i] > rHistogram[r]):
					r = i
				if (gHistogram[i] > gHistogram[g]):
					g = i
				if (bHistogram[i] > bHistogram[b]):
					b = i
			
			r = rTotal[r] / rHistogram[r]
			g = gTotal[g] / gHistogram[g]
			b = bTotal[b] / bHistogram[b]
			if(index < len(new_ar)):
				new_ar[index] = (r, g, b)
			else:
				new_ar.append((r, g, b))
			index+=1

   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('a.jpg')
	new = oil(im)
	new.save('a_oil.jpg')
	