from tkinter import *
from random import *
class pixelfield:
	def __init__(self,height,width,sidecell,window,colors=["white"]):
		self.height=height*sidecell
		self.width=width*sidecell
		self.sidecell=sidecell
		self.colors=colors
		self.coordinatesystem = []		
		for y in range(0,height):
			yarr=[]
			for x in range(0,width):
				coord = [(x*sidecell,y*sidecell),
             (x*sidecell+sidecell,y*sidecell+sidecell)]
				yarr.append(coord.copy())
			self.coordinatesystem.append(yarr.copy())
		grey=0
		red=0
		blue=0
		white=0
		self.colorblocks={} 							
		for y in range(height):
			for x in range(width):
				col=choice(colors)
				self.colorblocks[(y,x)]=col
				if col == "blue":
					blue+=1
				elif col == "red":
					red+=1
				elif col =="grey":
					grey+=1
				else:
					white+=1
		print("Серый: ",grey,"\nСиний: ",blue,"\nКрасный: ",red,"\nБелый: ",white)
		self.window=window
		self.canvas=Canvas(window,height=self.height,width=self.width)
		self.canvas.pack()

	def printfield(self):
		for y in range(self.height//self.sidecell):
			for x in range(self.width//self.sidecell):
				self.canvas.create_rectangle(self.coordinatesystem[y][x],fill=self.colorblocks[(y,x)])
	def randomgeneration(self):
		grey=0
		red=0
		blue=0
		white=0
		for y in range(self.height//self.sidecell):
			for x in range(self.width//self.sidecell):
				col=choice(self.colors)
				self.colorblocks[(y,x)]=col
				if col == "blue":
					blue+=1
				elif col == "red":
					red+=1
				elif col =="grey":
					grey+=1
				else:
					white+=1
		print("\n"*1000)
		print("Серый: ",grey,"\nСиний: ",blue,"\nКрасный: ",red,"\nБелый: ",white)


	def fillcell(self,coord,color):
		self.colorblocks[coord]=color

	def colorcell(self,coord):
		return self.colorblocks[coord]
	
	def getcolors(self):
		return self.colorblocks
	

	