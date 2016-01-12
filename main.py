#!/usr/bin/env python
import random
import webbrowser
import tempfile


IMAGE_SIZE_X = 1000
IMAGE_SIZE_Y = 1000
IMAGE_BUFFER = 50


TEMPLATE_PIE = '''
<path fill="#fff" d='M 55,5 A 50,50 0 1,1 5,55'/>
<path fill="#f4f4f4" d='M 55,5 A 50,50 0 0,0 5,55 l 50,0 0,-50 z'/>
'''

TEMPLATE_FILE = '''
<path fill="#fff" d="M 60,10 l -40,0 q -10,0 -10,10 l 0,90 q 0,10 10,10 l 60,0 q 10,0 10,-10 l 0,-70z l 0,20 q 0,10 10,10 l 20,0"/>
'''

TEMPLATE_DATA = '''
<path fill="#fff" d='M 5,5 l 80,0 0,100 -80,0 0,-100 m 10,10 l 40,0 m -40,10 l 60,0 m -60,10 l 50,0 m -50,20 l 60,0 m -60,10 l 30,0 m -30,10 l 60,0 m -60,10 l 60,0 m -60,10 l 30,0'/>
'''

TEMPLATE_GRAPH = '''
    <path fill="#fff" d="M 5,5 l 0,100 100,0 0, -100z"/>
    <path stroke="#f4f4f4" d="M 5,25 l 100,0 m -100,20 l 100,0 m -100,20 l 100,0 m -100,20 l 100,0 " />
    <path fill="#f4f4f4" d="M 5, 105 l 10,-40 10,10 10,-50 10,70 10,5 10,-50 10,10 10,20 10,10 10,15z"/>
'''

TEMPLATE_G = '''
<g transform="translate({x}, {y}) rotate({r})" fill="none" stroke="#eee" stroke-width="4">{d}</g>
'''

TEMPLATE_SVG = '''
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {sizex} {sizey}" style="width: 500px; border: 1px solid blue;">{d}</svg>
'''


def random_location(data):
	return TEMPLATE_G.format(
		x=random.randint(IMAGE_BUFFER, IMAGE_SIZE_X - IMAGE_BUFFER),
		y=random.randint(IMAGE_BUFFER, IMAGE_SIZE_Y - IMAGE_BUFFER),
		r=random.randint(0, 360),
		d=data
	)

def random_element():
	return random.choice([TEMPLATE_FILE, TEMPLATE_PIE, TEMPLATE_DATA, TEMPLATE_GRAPH])

def generate_bg():
	elements = []
	for x in range(max([IMAGE_SIZE_X, IMAGE_SIZE_Y]) / 30):
		elements.append(random_location(random_element()))

	return TEMPLATE_SVG.format(sizex=IMAGE_SIZE_X, sizey=IMAGE_SIZE_Y, d=''.join(elements))


if __name__ == '__main__':
	with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as ouf:
		for i in range(100):
			ouf.write(generate_bg())
		
		webbrowser.open_new_tab('file://' + ouf.name)
		