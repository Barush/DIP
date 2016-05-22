import numpy as np 
from scipy.misc import toimage
import os

THRESH = 1e-15

def load_array(path, filename):
	arr = np.loadtxt(path+filename)
	return arr

def main():
	files = os.listdir("../results/masks/sigm/01/origsize/")
	for f in files:
		filename = os.path.splitext(f)[0]
		#print filename
		arr = load_array("../results/masks/sigm/01/origsize/", f)
		low_i = arr < THRESH
		high_i = arr > THRESH
		arr[low_i] = 0
		arr[high_i] = 1
		im = toimage(arr)
		im.save("../results/masks/sigm/01/imgs/"+filename)



if __name__ == '__main__':
	main()

