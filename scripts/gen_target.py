import numpy as np
import os

TRUEVAL = 1
FALSEVAL = 0

def setSpz(trg, start_r, stop_r, start_c, stop_c):
	for r in range(len(trg)):
		for c in range(len(trg[0])):
			if((r >= start_r) & (r <= stop_r)):
				if((c >=  start_c) & (c <= stop_c)):
					#print "here"
					trg[r][c] = TRUEVAL

	#for i in range(18):
	#	print trg[i]

	return trg

def compress(arr):
	cmpr=np.full((13, 13), FALSEVAL, dtype=int)
	for r in range(13):
		for c in range(13):
			truecnt = 0
			for i in range(17):
				for j in range(25):
					if arr[17*r + i][25*c + j] == TRUEVAL:
						truecnt+=1
			if truecnt > (r*c/2):
				cmpr[r][c] = TRUEVAL

	return cmpr

def main():
	coords = open("../data/lists/spz_coords.csv", "r")
	print coords
	for line in coords:
	#line = "out_006460+section18-0.jpg, 113, 78, 136, 84, 239, 12, 253, 18, 0, 0, 0, 0, 0, 0, 0, 0"
	#print line
		line.rstrip('\n')
		line_arr = line.split(",")
		filename = line_arr[0]
		trg = np.zeros((227,332), dtype = np.int)
		for i in range(4):
			start_c = int(line_arr[4*i + 1])
			start_r = int(line_arr[4*i + 2])
			stop_c = int(line_arr[4*i + 3])
			stop_r = int(line_arr[4*i + 4])
			#print start_c, start_r, stop_c, stop_r
			if((start_r != 0) | (start_c != 0) | (stop_r != 0) | (stop_c != 0)):
				#print "Let's set it. Now."
				trg = setSpz(trg, start_r, stop_r, start_c, stop_c)

		np.savetxt("../data/targets/sigm_0-1/origsize/" + os.path.basename(filename) + "_target", trg, fmt='%i')
		cmpr = compress(trg)
		np.savetxt("../data/targets/sigm_0-1/compressed/" + os.path.basename(filename) + "_target", cmpr, fmt='%i')
	#np.savetxt("test", trg, fmt='%i')

	#for i in range(20):
	#	print trg[i]

if __name__ == '__main__':
	main()
