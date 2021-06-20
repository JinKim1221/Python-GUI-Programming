import time
from PIL import ImageGrab

time.sleep(5) # wait for 5 sec for user to get ready

for i in range(1, 11) : # save 10 images every two seconds
    img = ImageGrab.grab() # get the current screen image
    img.save("image{}.png".format(i)) # save as a file(image1.png ~ image10.png)
    time.sleep(2)