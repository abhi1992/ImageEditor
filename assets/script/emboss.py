import math
from PIL import Image
azimuth = 135.0 * math.pi / 180.0
elevation = 30.0 * math.pi / 180
emboss = False
width45 = 3.0
pixelScale = 2.5
def emboss(image, emboss=True):

	''''''

	import math
	ar = list(image.getdata())
	new_ar = []
	width, height = image.size
	bumpMapWidth = width
	bumpMapHeight = height
	bumpPixels = []
	index=0
	for i in range(0, len(ar)):
		bumpPixels.append((ar[i][0]+ar[i][1]+ar[i][2])/3)

	Lx = int(math.cos(azimuth) * math.cos(elevation) * pixelScale)
	Ly = int(math.sin(azimuth) * math.cos(elevation) * pixelScale)
	Lz = int(math.sin(elevation) * pixelScale)
	print Lx, Ly, Lz
	Nz = int(6 * 255 / width45)
	Nz2 = Nz * Nz
	NzLz = Nz * Lz

	background = Lz

	bumpIndex = 0


	for y in range(0, height):
	 	
		s1 = bumpIndex
		s2 = s1 + bumpMapWidth
		s3 = s2 + bumpMapWidth

		for x in range(0, width):

			if (y != 0 and y < height-2 and x != 0 and x < width-2) :
				Nx = bumpPixels[s1-1] + bumpPixels[s2-1] + bumpPixels[s3-1] - bumpPixels[s1+1] - bumpPixels[s2+1] - bumpPixels[s3+1]
				Ny = bumpPixels[s3-1] + bumpPixels[s3] + bumpPixels[s3+1] - bumpPixels[s1-1] - bumpPixels[s1] - bumpPixels[s1+1]
				NdotL = Nx*Lx + Ny*Ly + NzLz
				if (Nx == 0 and Ny == 0):
					shade = background
					# print 1
				elif (NdotL < 0):
					shade = 0
					# print 2
				else:
					# print 3
					shade = int(NdotL / math.sqrt(Nx*Nx + Ny*Ny + Nz2))
			else:
				# print y != 0 , y < height-2 , x != 0 , x < width-2
				shade = background

			if (emboss):
				r = ar[index][0]*shade
				g = ar[index][1]*shade 
				b = ar[index][2]*shade 
				# print shade, r, g, b
				new_ar.append((r, g, b))
				index+=1
			else:
				new_ar.append((shade, shade, shade))
				index+=1

			s1+=1
			s2+=1 
			s3+=1

		bumpIndex += bumpMapWidth
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('aa.jpg')
	new = emboss(im)
	new.save('aa_emboss.jpg')