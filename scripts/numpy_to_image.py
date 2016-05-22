import numpy as np 
from scipy.misc import toimage
import os


def load_array(path, filename):
	arr = np.loadtxt(path+filename)
	return arr

def main():
	files = os.listdir("../results/masks/relu/origsize/")
	for f in files:
		filename = os.path.splitext(f)[0]
		#print filename
		arr = load_array("../results/masks/relu/origsize/", f)
		im = toimage(arr)
		im.save("../results/masks/relu/imgs/"+filename)



if __name__ == '__main__':
	main()

