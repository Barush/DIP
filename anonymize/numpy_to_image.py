import numpy as np 
from scipy.misc import toimage
import os

def load_array(path, filename):
	arr = np.loadtxt(path+filename)
	return arr

def conv(cafferoot):
	files = os.listdir(cafferoot+"/masks_origsize")
	os.mkdir("masks_img")
	for f in files:
		filename = os.path.splitext(f)[0]
		print filename
		arr = load_array(cafferoot+"/masks_origsize/", f)
		im = toimage(arr)
		im.save(cafferoot+"/masks_img/"+filename)



if __name__ == '__main__':
	conv()

