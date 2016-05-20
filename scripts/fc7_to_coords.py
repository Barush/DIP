from keras.models import model_from_json
from keras.layers import Dense, Dropout, Activation, Convolution2D
from keras.optimizers import SGD
from keras.models import Sequential
import numpy as np
import os


class FC7_loader():
	target = np.empty([0, 4], dtype=int)
	data = np.empty([0,4096])	

	def __init__(self):
		dataset = open("../data/lists/oneimgtest.csv", 'r')
		
		#item = next(dataset)
		for item in dataset:
			item = item.rstrip()
			line = item.split(",")
			filename = os.path.basename(line[0]).strip('"')+".txt"
			#print filename
			fc7_line = np.loadtxt('../data/fc7/'+filename)
		#	print "fc7:", fc7_line
		#	print "-->",len(fc7_line)
			self.data = np.append(self.data, [fc7_line], axis = 0)
		dataset.close()

def main():
	modelfile = open('fc7_regression_architecture_relu.json', 'r')
	jsonmodel = next(modelfile)

	model = model_from_json(jsonmodel)
	model.load_weights('fc7_regression_weights_relu.h5')
	model.compile(optimizer='sgd', loss='mse')

	dataset = FC7_loader()

	prediction = model.predict(dataset.data);
	print prediction.shape

	f = open("../data/lists/oneimgtest.csv", 'r')
	trainlist = []
	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)

	print "Pred len: ", len(prediction)
	print "Trainlist len: ", len(trainlist)
	
	for i in range(len(prediction)):
		np.savetxt(str(trainlist[i])+".txt", prediction[i])

if __name__ == '__main__':
	main()
