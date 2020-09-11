from engine import *
import engine
from sizegete import *
xs = []
ys= []
images = []
ispl = []
b= 1
ims = []

l = 0



def render(image,x,y,a =0):

    global xs,ys,images,l,ispl,ims
    xs.append(x)
    ys.append(y)
    images.append(image)
    ispl.append(a)
    ims.append(sizeget(image))
    l += 1
    return l,image,x,y,ims
