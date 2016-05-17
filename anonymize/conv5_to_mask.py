from keras.models import model_from_json
import numpy as np
import os


def load_conv5(datalist, size, path):
	data = np.zeros([size, 256, 13, 13])
	f_datalist = open(datalist, 'r')
	i = 0

	for line in f_datalist:
		for f in range(255):
			philter = np.loadtxt(path+"/conv5/"+str(f)+"/"+os.path.basename(line.strip())+".txt")
			for r in range(13):
				for c in range(13):
					assert i < 1992, "it's i!"
					data[i][f][r][c] = philter[r][c]
		i+=1

	return data

def count_lines(filename):
	with open(filename) as f:
		for cnt, l in enumerate(f):
			pass
	return cnt + 1




def convert(anonympath, cafferoot):
	modelfile = open(anonympath+'/plate_detection/architecture.json', 'r')
	jsonmodel = next(modelfile)

	model = model_from_json(jsonmodel)
	model.load_weights(anonympath+'/plate_detection/weights.h5')
	model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])

	linecnt = count_lines("truelist.txt")

	dataset = load_conv5("truelist.txt", linecnt, cafferoot)

	prediction = model.predict(dataset);
	#print prediction.shape

	f = open("truelist.txt", 'r')
	trainlist = []
	for line in f:
		line = line.strip()
		#print line
		trainlist.append(line)

	#print "Pred len: ", len(prediction)
	#print "Trainlist len: ", len(trainlist)
	
	os.mkdir("masks")
	for i in range(len(prediction)):
		np.savetxt("masks/"+str(os.path.basename(trainlist[i]))+".txt", prediction[i][0])



if __name__ == '__main__':
	convert()