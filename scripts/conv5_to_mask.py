from keras.models import model_from_json
from keras.layers import Dense, Dropout, Activation, Convolution2D
from keras.optimizers import SGD
from keras.models import Sequential
import numpy as np


def load_conv5(datalist, size):
	data = np.zeros([size, 255, 13, 13])
	f_datalist = open(datalist, 'r') 
	i = 0

	for line in f_datalist:
		for f in range(255):
			philter = np.loadtxt("/home/mapy/cafe_build/python/conv5/10000/"+str(f)+"/"+line.strip()+".txt")
			for r in range(13):
				for c in range(13):
					assert i < 1992, "it's i!"
					data[i][f][r][c] = philter[r][c]
		i+=1

	return data


def linecnt(file):
	with open(file) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def main():
	modelfile = open('test.json', 'r')
	jsonmodel = next(modelfile)

	model = model_from_json(jsonmodel)
	model.load_weights('conv5_regression_weights_relu_1test.h5')
	model.compile(optimizer='sgd', loss='mse')

	datalen = linecnt("../data/lists/oneimgtest.csv")
	dataset = load_conv5("../data/lists/oneimgtest.csv", datalen)

	prediction = model.predict(dataset);
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
		np.savetxt(str(trainlist[i])+".txt", prediction[i][0])

if __name__ == '__main__':
	main()
