import numpy as np
import subprocess as sp
import os
import sys, getopt
import caffe


def run(model_file, pretrained_net, crops_path, caffe_root):
	sys.path.insert(0, caffe_root + 'python')

	caffe.set_device(1)
	caffe.set_mode_gpu()
	#net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)
	#print net.inputs

	net = caffe.Classifier(model_file, pretrained_net,
	                       mean=np.load(caffe_root + '/python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1),
	                       channel_swap=(2,1,0),
	                       raw_scale=255,
	                       image_dims=(227, 227))

	#img = 'out_002187+section0-0.jpg'

	images = os.listdir(crops_path)
	images.sort()

	os.mkdir("data/relu5")
	for i in range(255):
		os.mkdir("data/relu5/"+str(i))

	true_f = open("results/cars/spz_true.csv", 'w')

	for img in images:
		print img
		img = crops_path+'/'+img
		input_image = caffe.io.load_image(img)
		prediction = net.predict([input_image]) 
		#print net.blobs
		#data = net.blobs['fc7'].data[0]
		#np.savetxt("data/fc7/"+os.path.basename(img)+".txt", data)
		for i in range(255):
			data = net.blobs['relu5'].data[0][i]
			np.savetxt("data/relu5/"+str(i)+"/"+os.path.basename(img)+".txt", data)
		print prediction[0].argmax()
		if prediction[0].argmax() == 1:
			true_f.write(img+"\n")

	true_f.close()
