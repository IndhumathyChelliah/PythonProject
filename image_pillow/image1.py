
from PIL import Image
import os
#image2=Image.open("orange.jpg")
#image2.show()
#image2.save("orange.png")
size_300=(300,300)
for f in os.listdir('.'):
    if f.endswith("jpg"):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))
        #i.thumbnail(size_300)
        #i.save('300/{}_300.jpg'.format(fn))

image2=Image.open("orange.jpg")
#image2.rotate(90).save("orange_mod.jpg")
image2.convert(mode="L").save("orange_bl.jpg")
