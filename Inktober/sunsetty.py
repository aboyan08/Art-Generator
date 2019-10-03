from PIL import Image, ImageDraw
from colors import colors
import random
import math

class Sun:
    left = 112
    right = 212
    top = 121
    bottom = 221
    radius = (bottom-top)/2
    y_offset = 0
    start = 180
    end = 0

img = Image.new('RGB', (512,512), 'black')

frames = 100

sky_color = list(colors["periwinkle"])

for frame in range(frames):
    """ Draw Background """
    pixels = img.load()
    for i in range(img.size[0]):
      for j in range(img.size[1]):
        pixels[i,j] = (sky_color[0]+(171-j)//2, sky_color[1]+(171-j)//3, sky_color[2]+(171-j)//4)
    draw = ImageDraw.Draw(img)
    
    draw.line((0, 171, 512, 171), fill=colors["white"])

    """ Draw Sky """
    for i in range(0, img.size[0], 40):
      j = 5
      increment = 18
      while j < 171:
        left = random.random()*20-5
        right = random.random()*20+5
        draw.line((i-left, j, i+right, j), fill=colors["white"], width=3)
        j += increment
        increment -= 1

    """ Draw Road """
    for i in range(64, img.size[0], 64):
      draw.line(((256-i)*1.5+256, 512, 300, 171), fill=colors["white"])

    """ Draw Sun """
    draw.chord((Sun.left, Sun.top+Sun.y_offset, Sun.right, Sun.bottom+Sun.y_offset), start=Sun.start, end=Sun.end, fill=colors["white"])

    """ Save Frame """
    img.save("output/frame" + str(frame).zfill(5) + ".png")

    """ Update Sun """
    Sun.y_offset += 0.5
    end_rads = math.acos(Sun.y_offset/Sun.radius)
    Sun.end = math.degrees(end_rads) - 90
    Sun.start = 180 - Sun.end

    """ Update Colors """
    if frame < 50:
        sky_color[0] += 2
        sky_color[1] -= 1
    else:
        sky_color[0] -= 4
        sky_color[1] -= 2
    sky_color[2] -= 2

    """ Output Progress """
    if frame % 33 == 0:
        print(str(frame) + " of " + str(frames))




    
