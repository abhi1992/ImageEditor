def block(image, block_size=5):
	'''
	int w = Math.min( blockSize, width-x );
    int h = Math.min( blockSize, height-y );
    int t = w*h;
    getRGB( src, x, y, w, h, pixels );
    int r = 0, g = 0, b = 0;
    int argb;
    int i = 0;
    for ( int by = 0; by < h; by++ ) {
        for ( int bx = 0; bx < w; bx++ ) {
            argb = pixels[i];
            r += (argb >> 16) & 0xff;
            g += (argb >> 8) & 0xff;
            b += argb & 0xff;
            i++;
        }
    }
    argb = ((r/t) << 16) | ((g/t) << 8) | (b/t);
	'''
	ar = list(image.getdata())
	new_ar = []
	width, height = image.size
	pixels = []
	for i in range(0, width, block_size):
		for j in range(0, height, block_size):
			w = math.min(block_size, width - i)
			h = math.min(block_size, height - j)
			t = w*h

		
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

def random(Red, Green, Blue, amount):
	import random
	f = (int)(random.random()*amount)
	
	return (Red - f, Green - f, Blue - f)

def uniform(Red, Green, Blue, amount):
	import random
	f = (int)(random.uniform()*amount)
	
	return (Red - f, Green - f, Blue - f)

def gauss(Red, Green, Blue, amount):
	import random
	f = (int)(random.gauss()*amount)
	
	return (Red - f, Green - f, Blue - f)

def noise(image, mode, amount=90):


	ar = list(image.getdata())
	new_ar = []
	for pixel in ar:
		Red = pixel[0]
		Green = pixel[1]
		Blue = pixel[2]

   		r,g,b = mode(Red, Green, Blue, amount)
   		new_ar.append((r, g, b))
   	new_image = Image.new("RGB", image.size, "white")
   	new_image.putdata(new_ar)
   	return new_image

def scratch(image, density=.1, angle=0, angleVariation=1.0, width=0.5, length=0.5, color=128, seed=0):
	'''
	private float density = 0.1f;
    private float angle;
    private float angleVariation = 1.0f;
    private float width = 0.5f;
    private float length = 0.5f;
    private int color = 0xffffffff;
    private int seed = 0;

    if ( dst == null )
            dst = createCompatibleDestImage( src, null );

        int width = src.getWidth();
        int height = src.getHeight();
        int numScratches = (int)(density * width * height / 100);
        float l = length * width;
        Random random = new Random( seed );
        Graphics2D g = dst.createGraphics();
        g.setRenderingHint( RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON );
        g.setColor( new Color( color ) );
        g.setStroke( new BasicStroke( this.width ) );
        for ( int i = 0; i < numScratches; i++ ) {
            float x = width * random.nextFloat();
            float y = height * random.nextFloat();
            float a = angle + ImageMath.TWO_PI * (angleVariation * (random.nextFloat() - 0.5f));
            float s = (float)Math.sin( a ) * l;
            float c = (float)Math.cos( a ) * l;
            float x1 = x-c;
            float y1 = y-s;
            float x2 = x+c;
            float y2 = y+s;
            g.drawLine( (int)x1, (int)y1, (int)x2, (int)y2 );
        }
        g.dispose();
	'''

	width, height = image.size
	numScratches = (int) (density*width*height/100)
	l = length*width
	import random, math, ImageDraw
	draw = ImageDraw.Draw(image)
	angle = 0
	for i in range(0, numScratches):
		x = width * random.random()
		y = height * random.random()
		a = angle + 2*math.pi *(angleVariation * random.random() - 0.5)
		s = math.sin(a)*l
		c = math.cos(a)*l
		x1 = x - c
		y1 = y-s
		x2 = x + c
		y2 = y + s
		draw.line((x1, y1, x2, y2), fill=(color, color,color))
	del draw
	return image

if __name__ == '__main__':
	from PIL import Image
	im = Image.open('a.jpg')
	# new = noise(im, gauss)
	# new.save('noise_gauss.jpg')
	new = scratch(im)
	new.save('scratch.jpg')
	# new = noise(im, random)
	# new.save('noise_uniform.jpg')

