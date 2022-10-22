import time
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
		
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

image1 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, k, y, y, y, y, k, y,
         y, y, k, k, k, k, y, y,
         w, y, y, y, y, y, y, w
]

sense.set_pixels(image1)
time.sleep(1)


image2 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, y, y, y, y, y, y,
         y, k, k, k, k, k, k, y,
         w, y, y, y, y, y, y, w
]

sense.set_pixels(image2)
time.sleep(1)

image3 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image3)
time.sleep(1)
		
image4 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, b, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image4)
time.sleep(1)				


image5 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, b, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image5)
time.sleep(1)
		
image6 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, b, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image6)
time.sleep(1)		

image7 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, b, w
]		
		
sense.set_pixels(image7)
time.sleep(1)		
		
image8 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image8)
time.sleep(1)		
		
image9 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, b, y, y, y, b, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image9)
time.sleep(1)

image10 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, b, y, y, y, b, y,
         y, y, b, k, k, k, b, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image10)
time.sleep(1)

image11 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, b, y, y, y, b, y,
         y, y, b, k, k, k, b, y,
         y, k, b, y, y, y, b, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image11)
time.sleep(1)

image12 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, b, y, y, y, b, y,
         y, y, b, k, k, k, b, y,
         y, k, b, y, y, y, b, y,
         w, y, b, y, y, y, b, w
]		
		
sense.set_pixels(image12)
time.sleep(2)

image13 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, b, k, k, k, b, y,
         y, k, b, y, y, y, b, y,
         w, y, b, y, y, y, b, w
]		
		
sense.set_pixels(image13)
time.sleep(1)

image14 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, b, y, y, y, b, y,
         w, y, b, y, y, y, b, w
]		
		
sense.set_pixels(image14)
time.sleep(1)

image15 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, b, y, y, y, b, w
]		
		
sense.set_pixels(image15)
time.sleep(1)

image16 = [w, y, y, y, y, y, y, w,
         y, y, y, y, y, y, y, y,
         y, k, k, y, y, k, k, y,
         y, k, c, y, y, k, c, y,
         y, y, y, y, y, y, y, y,
         y, y, k, k, k, k, y, y,
         y, k, y, y, y, y, k, y,
         w, y, y, y, y, y, y, w
]		
		
sense.set_pixels(image16)
time.sleep(1)
		
		
		
		
		
		
		
		