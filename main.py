from pixelfield import *
from tkinter import *
from random import*
from time import*

window = Tk()
width=20
height=20
sidecell=30
world = pixelfield(height,width,sidecell,window,["grey","blue","white","red"])
world.printfield()

def init():
	world.randomgeneration()
	world.printfield()

	game()

def getlivecell(coord):
	redcell=0
	bluecell=0
	y1=coord[0]-1
	y2=coord[0]+2
	x1=coord[1]-1
	x2=coord[1]+2
	if y1<0:
		y1=0
	if y2>height:
		y2=height
	if x1<0:
		x1=0
	if x2>width:
		x2=width
	for y in range(y1,y2):
		for x in range(x1,x2):
			if ((y,x)!=coord) and world.colorblocks[(y,x)]=="red":
				redcell+=1
			if ((y,x)!=coord) and world.colorblocks[(y,x)]=="blue":
				bluecell+=1
	return [redcell,bluecell]

def game():
	while True:
		world.canvas.update()
		colorblockscop=world.colorblocks.copy()
		for y in range(height):
			for x in range(width):
				if colorblockscop[(y,x)]=="white":
					if getlivecell((y,x))[0]==3:
						world.colorblocks[(y,x)]="red"
					elif getlivecell((y,x))[1]==3:
						world.colorblocks[(y,x)]="blue"
				elif colorblockscop[(y,x)]=="blue":
					if getlivecell((y,x))[1]>=4 or getlivecell((y,x))[1]<=1 :
						world.colorblocks[(y,x)]="white"
				elif colorblockscop[(y,x)]=="red":
					if getlivecell((y,x))[0]>3 or getlivecell((y,x))[0]<2:
						world.colorblocks[(y,x)]="white"
		sleep(0.5)
		world.printfield()


btn_create=Button(text="генерировать и запустить новый океан",command = lambda :init())
btn_create.pack()

mainloop()