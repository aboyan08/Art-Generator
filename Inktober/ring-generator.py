from PIL import Image, ImageDraw
from colour import Color
import random

def colour_convert(rgb):
    """ Convert 1.0 max floats to 255 max ints """
    r, g, b = rgb
    return (int(r*255), int(g*255), int(b*255))
    
class Ring:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.alpha = 255
        self.rgba = colour_convert(self.color.rgb) + (self.alpha,)

    def update(self):
        self.radius += 2
        self.alpha -= 10
        if self.alpha < 0:
            self.alpha = 0
        self.rgba = colour_convert(self.color.rgb) + (self.alpha,)

def make_ring():
    x = random.random()*img.size[0]
    y = random.random()*img.size[1]
    radius = 1
    color = Color(rgb=(random.random(), random.random(), random.random()))
    return Ring(x, y, radius, color)


img = Image.new('RGB', (512,512), 'black')

periwinkle = Color("#CCCCFF")

rings = [make_ring() for _ in range(15)]

frames = 300

for frame in range(frames):
    """ Draw Background """
    pixels = img.load()
    for i in range(img.size[0]):
      for j in range(img.size[1]):
        pixels[i,j] = (int(periwinkle.red*255+(i-j)//2), int(periwinkle.green*255+(i-j)//3), int(periwinkle.blue*255+(i-j)//4))

    """ Draw Rings """
    draw = ImageDraw.Draw(img, 'RGBA')
    for ring in rings:
        x = ring.x
        y = ring.y
        radius = ring.radius
        rgba = ring.rgba
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), outline=rgba)

    """ Save Frame """
    img.save("output/frame" + str(frame).zfill(5) + ".png")

    """ Update & Remove Rings """
    rings_to_remove = []
    for ring in rings:
        ring.update()
        if ring.alpha <= 0:
            rings_to_remove.append(ring)
    for ring in rings_to_remove:
        rings.remove(ring)
            
    """ Add Ring """
    if True: #frame % 3 == 0:
        rings.append(make_ring())

    """ Output Progress """
    if frame % 100 == 0:
        print(str(frame) + " of " + str(frames_total))



"""
This is the command line command to make the mp4
You need ffmpeg installed, then open powershell in the output folder and use this cmd
(Theoretically this could be done from python with the subprocess.call thing but I haven't worked on that yet)
"""
cmd = "ffmpeg -r 30 -i frame%05d.png -vcodec mpeg4 -b:v 5000k -y output_movie.mp4"
#subprocess.call(cmd, shell=True)

