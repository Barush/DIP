from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Convolution2D
from keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
from keras import backend as K

import numpy as np
import subprocess as sp
import os.path  

class FC7_loader():
	target = np.empty([0, 4], dtype=int)
	data = np.empty([0,4096])	

	def __init__(self):
		dataset = open("../data/lists/spz_coords.csv", 'r')
		
		#item = next(dataset)
		for item in dataset:
			item = item.rstrip()
			line = item.split(",")
			filename = os.path.basename(line[0]).strip('"')+".txt"
			#print filename
			self.target = np.append(self.target, [[line[1], line[2], line[3], line[4]]], axis = 0)
			fc7_line = np.loadtxt('../data/fc7/'+filename)
		#	print "fc7:", fc7_line
		#	print "-->",len(fc7_line)
			self.data = np.append(self.data, [fc7_line], axis = 0)
		dataset.close()

def main():
	model = Sequential()
	model.add(Dense(512, input_dim=4096, init='uniform'))
	model.add(Activation('sigmoid'))
	model.add(Dense(128, init='uniform'))
	model.add(Activation('sigmoid'))
	model.add(Dense(32, init='uniform'))
	model.add(Activation('sigmoid'))
	model.add(Dense(4, init='uniform'))
	model.add(Activation('linear'))

	model.compile(optimizer='sgd', loss='mse')
	
	#trainset = np.random.rand(2, 2, 13, 13)
	#traintarget = np.zeros([2, 1,13,13])

	trainset = FC7_loader()

	model.fit(trainset.data, trainset.target, nb_epoch=100000, verbose = 2, validation_split = 0.2)

#	testset = load_conv5(testfile)
#	testtarget = load_trg(testfile)

	model_architecture = model.to_json()
	res = open('fc7_regression_architecture_relu.json', 'w')
	res.write(model_architecture)
	res.close()
	model.save_weights('fc7_regression_weights_relu.h5')

	#print model.metrics_names
#	score = model.evaluate(testset, testtarget, batch_size = 16)
#	print "Score ", i, ": ", score

if __name__ == '__main__':
	main()
