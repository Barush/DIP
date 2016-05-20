###############################################################################
#			BARBORA SKRIVANKOVA, xskriv01@stud.fit.vutbr.cz					  #
#							DIPLOMOVA PRACE									  #
#							FIT VUT V BRNE									  #
#						ANONYMIZACE SPZ VOZIDEL								  #
#			Vypracovano ve spolupraci se spolecnosti Seznam.cz				  #
#																			  #
#								2015/2016									  #
###############################################################################

import sys, getopt
import subprocess as sp
from anonymize import classify
from anonymize import conv5_to_mask as cnv2msk
from anonymize import reconstruct_mask as rec
from anonymize import numpy_to_image as num2img
import os


# nacteni parametru: 
#	- slozka obsahujici obrazky k anonymizaci
#	- slozka obsahujici ostatni skripty a konfiguraky (default: ./anonymize)
#	- slozka, kam maji byt ulozeny anonymizovane obrazky
class Params():
	srcpath = os.getcwd()+"/img"
	anonympath = os.getcwd()+"/anonymize"
	dstpath = os.getcwd()+"/img_anonymized"
	caffe_root = os.getcwd()

	def __init__(self, argv):
		try:
			opts, args = getopt.getopt(argv[1:],"hs:a:d:r:", ["help", "src=", "anonym=", "dst=", "root="])
		except getopt.GetoptError:
			print "Wrong params!"
			help()
			sys.exit(2)
	   
	   	for opt, arg in opts:
			if opt == '-h':
				help()
				sys.exit()
			elif opt in ("-s", "--src"):
				self.srcpath = arg
			elif opt in ("-a", "--anonym"):
				self.anonympath = arg
			elif opt in ("-d", "--dst"):
				self.dstpath = arg
			elif opt in ("-r", "--root"):
				self.caffe_root = arg

def help():
  	print '---'
  	print 'Usage: anonymize.py [-s <sourcepath> -a <anonympath> -d <destpath> -r <cafferoot>]'
  	print '\t<sourcepath> - path to a folder where images to anonymize are stored'
  	print '\t\tdefault: ./img'
  	print '\t<anonympath> - path to a folder with all anonymization scripts '
  	print '\t\tdefault: ./anonymize'
  	print '\t<destpath> - path to a folder where anonymized images are to be stored'
  	print '\t\tdefault: ./img_anonymized'	
  	print '\t<cafferoot> - path to a folder where caffe root is located'
  	print '\t\tdefault: folder where anonymize is located'	

def main(argv):

	#loadparams
	params = Params(argv)
	#print "Source path: ", params.srcpath
	#print "Anonym path: ", params.anonympath
	#print "Destination path: ", params.dstpath

	# crop:
	print "Creating crops..."
	sp.call(["./anonymize/crop.sh", params.srcpath])

	# classify:
	#	-> zavolani skriptu panorama_classify.py
	#	-> klasifikace vsech vstupu
	print "Classifying crops..."
	car_weights = params.anonympath+"/car_detection/panorama_spz_iter_10000.caffemodel"
	car_architecture = params.anonympath+"/car_detection/deploy.prototxt"
	crops_path = params.srcpath+"/crops"
	classify.run(car_architecture, car_weights, crops_path, params.caffe_root)


	# regression:
	#	-> zavolani skriptu regression.py
	#	-> vytvoreni masek pro jednotlive croppy
	

	#cnv2msk.convert(params.anonympath, params.caffe_root)
	#rec.reconstruct(params.caffe_root)
	num2img.conv(params.caffe_root)


	# blur:
	#	-> zavolani skriptu blur_spz.py
	#	-> dopocitani souradnic SPZ z masek
	#	-> anonymizace vybranych oblasti v puvodnim obrazku

	#	^^^ TODO: vstupni parametr - slozka obsahujici masky croppu ^^^
	#			  vstupni parametr - slozka obsahujici obrazky k anonymizaci
	#			  mapovani komprimovane masky na originalni (13*13 --> 332*227)
	#			  dopocet souradnic z masky




if __name__ == '__main__':
   	main(sys.argv)
