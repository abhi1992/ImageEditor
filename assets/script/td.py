from color_adjust import *
from dither import *
from PIL import Image
init(ditherOrdered8x8Matrix)
im_file = 'in.jpg'
folder = 'f'
filter_code = '0'
im = Image.open('/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+im_file)
new = dither(im)
output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/'+filter_code+"_"+im_file
out_file = open( output_filename, 'wb' )
new.save(out_file)