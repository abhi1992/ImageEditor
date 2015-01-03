import re
import numpy

def read_pgm(filename, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.

    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    """
    with open(filename, 'a+') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return numpy.fromstring(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height)
                            
                            ).reshape((int(height), int(width)))

def inverse_pgm(image):
    
    inverse = image
    i = 0
    for row in image:
        j=0
        for v in row:
            inverse[i][j] = 255-v
            j += 1
        i += 1
    print inverse
    return inverse

def write_pgm(filename, image):
    """
    """
    with open(filename, 'w') as f:
        buffer = f.write(image)
    
if __name__ == '__main__':
    image = read_pgm('b.pgm')
    inverse = inverse_pgm(image)
    write_pgm('out.pgm', inverse)
