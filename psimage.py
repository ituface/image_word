#coding:utf-8
import math
from PIL import Image,ImageDraw,ImageFont
import random
list=['你好','你好呀','你好呀你好呀']
one=Image.new("RGBA",(400,400),(155,205,155))
#one=Image.open('/Users/finup/Desktop/anacond361/newImg.png')
draw=ImageDraw.Draw(one)




#根据半径求坐标 以30度旋转，半径100
height,width=one.size
x=width/2
y=height/2
yuanzhou=360
banjing = 100
hudu = banjing / 5
cout=int(banjing//hudu)
print(cout)
i=0
fontsize=5
while True:
    while True:
       ysin=y-round(math.sin(math.radians(yuanzhou)),2)*banjing
       xcos=x-round(math.cos(math.radians(yuanzhou)),2)*banjing
       print(banjing)
       newfont = ImageFont.truetype(font='/Users/finup/Downloads/weuruan/msyhbd.ttf',
                                    size=fontsize)
       draw.text((xcos, ysin), '嘿', (random.randint(0,255), random.randint(0,255), random.randint(0,255)), font=newfont)
       yuanzhou-=hudu
       if yuanzhou<=5:
          break
    i+=1
    print(i)
    yuanzhou=360
    fontsize+=7
    banjing-=30
    if i==3:
     newfont = ImageFont.truetype(font='/Users/finup/Downloads/weuruan/msyhbd.ttf',size=30)
     draw.text((height / 2-8, width / 2-10), '嘿', (random.randint(0,255), random.randint(0,255), random.randint(0,255)), font=newfont)
     draw.text((40, 60), 'i  am  xy', (random.randint(0,255), random.randint(0,255), random.randint(0,255)), font=newfont)

     break

one.show()
one.save('touxiang.png','PNG')
