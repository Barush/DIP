from keras.models import model_from_json
from keras.layers import Dense, Dropout, Activation, Convolution2D
from keras.optimizers import SGD
from keras.models import Sequential
import numpy as np


def load_conv5(datalist, size):
	data = np.zeros([size, 255/8, 13, 13])
	f_datalist = open(datalist, 'r') 
	i = 0

	for line in f_datalist:
		for f in range(255/8):
			philter = np.loadtxt("../data/conv5/"+str(f)+"/"+line.strip()+".txt")
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
	modelfile = open('conv5_regression_architecture_sigm018.json', 'r')
	jsonmodel = next(modelfile)

	model = model_from_json(jsonmodel)
	model.load_weights('conv5_regression_weights_sigm018.h5')
	model.compile(optimizer='sgd', loss='mse')
	datalen = linecnt("../data/lists/spz/valset1-1.csv")
	dataset = load_conv5("../data/lists/spz/valset1-1.csv", datalen)

	prediction = model.predict(dataset);
	print prediction.shape

	f = open("../data/lists/spz/valset1-1.csv", 'r')
	trainlist = []
	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)

	print "Pred len: ", len(prediction)
	print "Trainlist len: ", len(trainlist)
	
	for i in range(len(prediction)):
		np.savetxt("../results/masks/sigm/01/"+str(trainlist[i])+".txt", prediction[i][0])

if __name__ == '__main__':
	main()
