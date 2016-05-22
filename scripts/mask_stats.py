import numpy as np
import sys

def count(itemslist, activation, variant):
	f = open(itemslist, 'r')

	print "TP, TN, FP, FN"

	for i, l in enumerate(f):
		truepos = 0
		trueneg = 0
		falsepos = 0
		falseneg = 0
	
		l = l.strip()
		expected = np.loadtxt("../data/targets/"+activation+variant+"/origsize/"+l+"_target")
		out = np.loadtxt("../results/masks/"+activation+variant+"/origsize/"+l+".txt")
		
		for r in range(len(expected)):
			for c in range(len(expected[0])):
				if expected[r][c] == 0:
					if out[r][c] == 0:
						trueneg+=1
					else:
						falsepos+=1
				else:
					if out[r][c] == 1:
						truepos+=1
					else:
						falseneg+=1
		print truepos,", ",trueneg,", ",falsepos,", ",falseneg 	

	f.close()
	

def main(argv):
	ilist = "../data/lists/spz_true.csv"
	activation = "relu"
	variant = "" 

	if(len(argv) == 1):
		ilist = argv[0]
	elif (len(argv) == 2):
		ilist = argv[0]
		activation = argv[1]
	elif (len(argv) == 3):
		ilist = argv[0]
		activation = argv[1]
		variant = argv[2]

	count(ilist, activation, variant)


if __name__ == '__main__':
	main(sys.argv[1:])
