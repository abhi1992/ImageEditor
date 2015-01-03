def filter_image(com=0, im=""):

    if int(com) == 1:
        return color_adjust(im, invert)

    if int(com) == 2:
        return color_adjust(im, posterize)

    if int(com) == 3:
        return color_adjust(im, channel_mix)

    if int(com) == 4:
        init(ditherOrdered8x8Matrix)
        return dither(im)

    if int(com) == 5:
        init(ditherCluster8Matrix)
        return dither(im)

    if int(com) == 6:
        init(ditherCluster4Matrix)
        return dither(im)

    if int(com) == 7:
        init(ditherCluster3Matrix)
        return dither(im)

    if int(com) == 8:
        init(dither90Halftone6x6Matrix)
        return dither(im)

    if int(com) == 9:
        init(ditherLines4x4Matrix)
        return dither(im)

    if int(com) == 10:
        init(ditherMagic2x2Matrix)
        return dither(im)

    if int(com) == 11:
        init(ditherMagic4x4Matrix)
        return dither(im)

    if int(com) == 12:
        init(dither_ordered_4x4)
        return dither(im)

    if int(com) == 13:
        init(ditherOrdered6x6Matrix)
        return dither(im)

    if int(com) == 14:
        init(dither_halftone_8x8)
        return dither(im)

    if int(com) == 15:
        init(dither_bayer_4x4)
        return dither(im)

    if int(com) == 16:
        return emboss(im)

    if int(com) == 17:
        return g.grayscale(im, g.invert)

    if int(com) == 18:
        return g.grayscale(im, g.luma)

    if int(com) == 19:
        return g.grayscale(im, g.desaturation)

    if int(com) == 20:
        return g.grayscale(im, g.max_decomposition)

    if int(com) == 21:
        return g.grayscale(im, g.min_decomposition)

    if int(com) == 22:
        return g.grayscale(im, g.min_decomposition)

    if int(com) == 23:
        return g.grayscale(im, g.custom_shade, 2)

    if int(com) == 24:
        return g.grayscale(im, g.custom_shade, 3)

    if int(com) == 25:
        
        return g.grayscale(im, g.custom_shade, 5)


    

if __name__ == '__main__':
    import sys
    from color_adjust import *
    from dither import *
    import grayscale as g
    from emboss import *
    from PIL import Image
    
    im_file = sys.argv[1]
    folder = sys.argv[2]
    com = sys.argv[3]
    
    if int(com) == 0:
        print "ekj"
        if im_file is None:
            im_file = "in.jpg";
        filter_code = "1"
        name = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'
        
        im = Image.open('/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+im_file)
        im_o = Image.open('/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/'+im_file)

        new = color_adjust(im, invert)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "2"
        new = color_adjust(im, posterize)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        new = color_adjust(im, channel_mix)
        filter_code = "3"
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)
        
        init(ditherOrdered8x8Matrix)
        filter_code = "4"
        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherCluster8Matrix)
        filter_code = "5"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherCluster4Matrix)
        filter_code = "6"
        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherCluster3Matrix)
        filter_code = "7"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(dither90Halftone6x6Matrix)
        filter_code = "8"

        new = dither(im_o)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherLines4x4Matrix)
        filter_code = "9"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherMagic2x2Matrix)
        filter_code = "10"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(ditherMagic4x4Matrix)
        filter_code = "11"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )

        new.save(out_file)

        init(dither_ordered_4x4)
        filter_code = "12"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )

        new.save(out_file)

        init(ditherOrdered6x6Matrix)
        filter_code = "13"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(dither_halftone_8x8)
        filter_code = "14"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        init(dither_bayer_4x4)
        filter_code = "15"

        new = dither(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "16"
        new = emboss(im)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "17"
        new = g.grayscale(im, g.invert)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "18"
        new = g.grayscale(im, g.luma)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "19"
        new = g.grayscale(im, g.desaturation)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "20"
        new = g.grayscale(im, g.max_decomposition)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "21"
        new = g.grayscale(im, g.min_decomposition)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)


        filter_code = "22"
        new = g.grayscale(im, g.min_decomposition)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "23"
        new = g.grayscale(im, g.custom_shade, 2)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "24"
        new = g.grayscale(im, g.custom_shade, 3)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

        filter_code = "25"
        new = g.grayscale(im, g.custom_shade, 5)
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/thumbnail/'+filter_code+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)

    else:

        if im_file is None:
            im_file = "in.jpg";

        im_o = Image.open('/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/'+im_file)
        
        new = filter_image(com, im_o)
        
        output_filename = '/home/abhishek/Documents/php/codeigniter/imageEditor/files/'+folder+'/'+com+"_"+im_file
        out_file = open( output_filename, 'wb' )
        new.save(out_file)