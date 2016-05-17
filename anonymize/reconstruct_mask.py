import numpy as np 
import os

def load_compressed(datalist, size, path):
	data = np.zeros([size, 13, 13], dtype = np.int)
	f_datalist = open(datalist, 'r')
	i = 0

	for line in f_datalist:
		mask = np.loadtxt("masks/"+os.path.basename(line.strip())+".txt")
		for r in range(13):
			for c in range(13):
				assert i < 1992, "it's i!"
				data[i][r][c] = mask[r][c]
		i+=1

	return data

def count_lines(filename):
	with open(filename) as f:
		for cnt, l in enumerate(f):
			pass
	return cnt + 1


def reconstruct(cafferoot):
	lines = count_lines("truelist.txt")
	data = load_compressed("truelist.txt", lines, cafferoot)

	f = open("truelist.txt", 'r')
	trainlist = []
	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)

	os.mkdir("masks_origsize")
	for c in range(len(trainlist)):
		orig_size = np.zeros((227, 332), dtype = int)
		for i in range(len(data[c])):
			for j in range(len(data[c][i])):
				if data[c][i][j] == 1:
					#print "[", str(i), "][", str(j),"]"
					for k in range(18):
						for l in range(26):
							orig_size[18*i + k][26*j + l] = 1

		np.savetxt("masks_origsize/"+os.path.basename(trainlist[c])+".txt", orig_size)


if __name__ == '__main__':
	reconstruct()