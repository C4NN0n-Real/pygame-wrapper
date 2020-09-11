
import pygame
from renderer import *
import renderer
from math import *
# code borrowed from javatpoint medium.com
#colors from www.rapidtables.com
red  = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
orangered = (255,69,0)
orange = (255,165,0)
pc  = 0
xa = []
ya = []
dists = []
pxa = []
pya = []
pia = []
js = 0
spd = 0
npc = []
dx = []
dy = []
la = 0
dox =[]
doy = []
ima = []
imd = []


#to make surface global
dis = ""
clock = pygame.time.Clock()



def start(resy = 800,resx = 600):
    pygame.init()
    global dis,dx,dy

    dis = pygame.display.set_mode((resy,resx))

def player(img,px,py,sp):
    global spd
    spd = sp
    render(img,px,py,1)


def move(j,mx,my,sp):
    global xa,ya
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        xa[js] -= sp
    if keys[pygame.K_d]:
        xa[js] += sp
    if keys[pygame.K_w]:
        ya[js] -= sp
    if keys[pygame.K_s]:
        ya[js] += sp

def gameloop(color = white):
    for i in range(renderer.l):
        dx.append(0)
        dy.append(0)
        dox.append(0)
        doy.append(0)
        dists.append(0)
        imd.append(0)



    gameloope(color)





def gameloope(color = white):
    dis.fill(color)
    clock.tick(30)
    while True:
          dis.fill(color)
          global js,xa,ya,spd,dist,npc,dx,dy,la,ima,imd
          xa = renderer.xs
          ya = renderer.ys
          ia = renderer.images
          la = renderer.l
          aa = renderer.ispl
          ima = renderer.ims


          for i in range(la):

            if aa[i] == 1:
                  i = js
                  move(js,xa[i],ya[i],spd)
            if js != i:
                  if xa[js] > xa[i]:
                      dx[i] = (sqrt(xa[js] -xa[i])**2)
                      dox[i] = round(dx[i],2)

                  elif xa[i] > xa[js]:
                      dx[i] = (sqrt(xa[i] - xa[js])**2)
                      dox[i] = round(dx[i],2)

                  if ya[js] > ya[i]:
                      dy[i] = (sqrt(ya[js] -ya[i])**2)
                      doy[i] = round(dy[i],2)

                  elif ya[i] > ya[js]:
                      dy[i] = (sqrt(ya[i] - ya[js])**2)
                      doy[i] = round(dy[i],2)
                  dists[i] = dox[i] + doy[i]

                 


            dis.blit(pygame.image.load(ia[i]),(xa[i],ya[i]))




          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

          pygame.display.update()
