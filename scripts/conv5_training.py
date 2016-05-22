from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Convolution2D
from keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
from keras import backend as K

import numpy as np
import subprocess as sp
import os.path  

def load_conv5(datalist, size, sample = 1):
	data = np.zeros([size, 255/sample, 13, 13])
	f_datalist = open(datalist, 'r')

	for i, line in enumerate(f_datalist):
		for f in range(255/sample):
			conv = f*sample
			philter = np.loadtxt("../data/conv5/"+str(conv)+"/"+line.strip()+".txt")
			for r in range(13):
				for c in range(13):
					data[i][f][r][c] = philter[r][c]
	f_datalist.close()
	return data

def load_trg(datalist, size):
	data = np.zeros([size, 1, 13, 13], dtype = np.int)
	f_datalist = open(datalist, 'r')

	for i, line in enumerate(f_datalist):
		mask = np.loadtxt("../data/targets/relu_0-255/compressed/"+line.strip()+"_target")
		for r in range(13):
			for c in range(13):
				data[i][0][r][c] = mask[r][c]
	
	f_datalist.close()
	return data

def linecnt(file):
	with open(file) as f:
		for i, l in enumerate(f):
			pass
	return i+1


def main():
	trainfile = "../data/lists/spz_true.csv"
	#testfile = "../data/lists/all.csv"	
	traincnt = linecnt(trainfile) 
	traintarget = load_trg(trainfile, traincnt)

	for i in range(8, 0, -1):
		model = Sequential()
		model.add(Convolution2D(1, 3, 3, border_mode = 'same', input_shape=(255/i, 13, 13)))
		model.add(Activation('relu'))
		# print Activation('relu').activation(np.ones(100))
		# return
		model.compile(optimizer='sgd', loss='mse')
		
		#trainset = np.random.rand(2, 2, 13, 13)
		#traintarget = np.zeros([2, 1,13,13])

		trainset = load_conv5(trainfile, traincnt, i)
		model.fit(trainset, traintarget, nb_epoch=1000, verbose = 2, validation_split = 0.2)

		#testcnt = linecnt(testfile)
		#testset = load_conv5(testfile, testcnt, i)
		#testtarget = load_trg(testfile, testcnt)

		model_architecture = model.to_json()
		open('conv5_regression_architecture_relu'+str(i)+'.json', 'w').write(model_architecture)
		model.save_weights('conv5_regression_weights_relu'+str(i)+'.h5')

		#print model.metrics_names
		#score = model.evaluate(testset, testtarget, batch_size = 16)
		#print "Score ", i, ": ", score

if __name__ == '__main__':
	main()
