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
	modelfile = open('../results/nets/conv5_regression_architecture_relu8.json', 'r')
	jsonmodel = next(modelfile)

	model = model_from_json(jsonmodel)
	model.load_weights('../results/nets/conv5_regression_weights_relu8.h5')
	model.compile(optimizer='sgd', loss='mse')
	datalen = linecnt("../data/lists/spz_true.csv")
	dataset = load_conv5("../data/lists/spz_true.csv", datalen)

	prediction = model.predict(dataset);
	print prediction.shape

	f = open("../data/lists/spz_true.csv", 'r')
	trainlist = []
	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)

	print "Pred len: ", len(prediction)
	print "Trainlist len: ", len(trainlist)
	
	for i in range(len(prediction)):
		np.savetxt("../results/masks/relu/compressed/"+str(trainlist[i])+".txt", prediction[i][0])

if __name__ == '__main__':
	main()
