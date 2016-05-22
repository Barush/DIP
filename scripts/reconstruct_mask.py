import numpy as np 

def load_compressed(datalist, size):
	data = np.zeros([size, 13, 13])
	f_datalist = open(datalist, 'r')

	for i, line in enumerate(f_datalist):
		mask = np.loadtxt("../results/masks/sigm/01/compressed/"+line.strip()+".txt")
		for r in range(13):
			for c in range(13):
				data[i][r][c] = mask[r][c]
	return data


def main():

	f = open("../data/lists/spz/valset1-1.csv", 'r')
	trainlist = []
	

	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)
	f.close()
	data = load_compressed("../data/lists/spz/valset1-1.csv", len(trainlist))

	for c in range(len(trainlist)):
		orig_size = np.zeros((227, 332))
		for i in range(len(data[c])):
			for j in range(len(data[c][i])):
				if data[c][i][j] != 0:
					#print "[", str(i), "][", str(j),"]"
					for k in range(17):
						for l in range(25):
							orig_size[17*i + k][25*j + l] = data[c][i][j]

		np.savetxt("../results/masks/sigm/01/origsize/"+trainlist[c]+".txt", orig_size)


if __name__ == '__main__':
	main()
