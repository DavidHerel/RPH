from utils import *

def calculate(data):
	"""Algorithm that creates increasing shape"""
	directions = [-1,1j,1,0-1j]
	direction_index = 0
	counter = 1
	switch = 0
	created_nodes = 0
	result = []
	length = len(data) - 1

	while(True):
		for direction in range(counter): 
			result.append(directions[direction_index % 4])
			created_nodes += 1
			if(direction == counter - 1):
				direction_index += 1
			if(length == created_nodes):
				break
		switch += 1
		if(switch % 2 == 0):
			counter += 1
		if(length == created_nodes):
			break
	return result 

if __name__ == "__main__":
	#read data from text file
	data = read_file_int("sequence.txt")
		
	result = calculate(data)

	#create text file with result sequence
	write_file("folding.txt", result)

