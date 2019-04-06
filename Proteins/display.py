from itertools import accumulate
import matplotlib.pyplot as plt
import numpy as np
from utils import *
from fold import calculate

def display(values, position):
	plt.figure()
	colors = {"red" : 1, "blue" : 0}
	coords = list_into_coords(position)
	index = 0	
	x, y = path_array(coords)
	#render lines which connets nodes of the graph
	plt.plot(x, y, zorder = 1, lw = 1)
	#render nodes, rendering depends on color and coordinates
	for color in values:
		if color == colors["red"]:   
			plt.scatter(x[index], y[index] , s=100, zorder = 2, c = 'r')
			index+=1
		else:
			plt.scatter(x[index], y[index], s=100, zorder = 2, c = 'b')
			index+=1
	
	plt.title('Protein folding')
	plt.show()
		
if __name__ == "__main__":
	#read data from text file
	values = read_file_int("sequence.txt")
	
	#read created sequence from fold generator
	coordinates = read_file("folding.txt")

	#render graph with nodes and lines
	display(values, coordinates)


