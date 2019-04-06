from itertools import accumulate

def read_file(file_name):
	"""Function reads data from text file and puts it into list of complex numbers"""
	file = open(file_name, "r", encoding="utf-8")
	data = file.read()
	file.close()

	result = []
	data = data.split()
	for node in data:
		node = complex(node)
		result.append(node)

	return result
	

def write_file(file_name, data):
	"""Function creates text file from generated list"""
	file = open(file_name, "w", encoding="utf-8")
	for node in data:
			string = str(node) + " "
			file.write(string)
	file.write("\n")
	file.close()

def list_into_coords(position):
	"""Function takes positions and creates coordinates from it"""
	coords = [0]
	coords.extend(accumulate(position)) 
	return coords
	
def read_file_int(file_name):
	"""Function reads data from text file and puts it into list of numbers"""
	file = open(file_name, "r", encoding="utf-8")
	data = file.read()
	file.close()

	result = []
	data = data.split()
	for node in data:
		node = int(node)
		result.append(node)

	return result

def path_array(array):
	"""Function that divides coordinates into two separated lists"""
	real = []
	imag = []
	for x in array:
		real.append(x.real)
		imag.append(x.imag)
	return real, imag
