import sys
import numpy as np

class Rectangle():

	def __init__(self, coords):
		self.x_A = round(float(coords[0])*332)
		self.y_A = round(float(coords[1])*227)
		self.x_B = round(float(coords[2])*332)
		self.y_B = round(float(coords[3])*227)
		self.width = abs(self.x_A - self.x_B)
		self.height = abs(self.y_A - self.y_B)

	def setCoords(self, coords):
		self.x_A = round(float(coords[0])*332)
		self.y_A = round(float(coords[1])*227)
		self.x_B = round(float(coords[2])*332)
		self.y_B = round(float(coords[3])*227)
		self.width = abs(self.x_A - self.x_B)
		self.height = abs(self.y_A - self.y_B)		

	def getArea(self):
		#print "area: ", self.width, " * ", self.height
		return (self.width * self.height)

	def xOK(self):
		return (self.x_B > self.x_A)

	def yOK(self):


		return (self.y_B < self.y_A)

	def switchCorners(self):
		#print "Switching corners"
		xa = min(self.x_A, self.x_B)
		xb = max(self.x_A, self.x_B)
		ya = max(self.y_A, self.y_B)
		yb = min(self.y_A, self.y_B)

		self.x_A = xa
		self.x_B = xb
		self.y_A = ya
		self.y_B = yb

def load_coords(filename):
	f = open(filename, 'r')	
	coords = np.empty([0, 4])
#	print coords

	for i, l in enumerate(f):
		l = l.strip()
		item = open("../results/coords/"+l+".txt", 'r')
		a = np.zeros(4)
		for j, n in enumerate(item):
			 a[j] = n
		coords = np.append(coords, [a], axis = 0)		
		item.close()

	f.close()	
	return coords	

def load_expectations(filename):
	f = open(filename, 'r')
	coords = np.empty([0,4])
	
 	for i, l in enumerate(f):
		l = l.strip()
		items = l.split(",")
		coords = np.append(coords, [[items[1], items[2], items[3], items[4]]], axis = 0)	

	f.close()
	print coords
	return coords


def count():
	coords_d = load_coords("../data/lists/spz_true.csv")
	coords_o = load_expectations("../data/lists/spz_coords.csv")
	#point = [x_A, y_A, x_B, y_B]
	#coords_o = [2,3,5,1]
	err = 0
	#print "original: ", coords_o
	#print "detected: ", coords_d

	print "Intersection, original, detected"

	for i in range(0, len(coords_d)):
		orig = Rectangle(coords_o[i])
		if not (orig.xOK() & orig.yOK()):
			orig.switchCorners()

		#coords_d = [4,2,7,1]
		det = Rectangle(coords_d[i])
		if not (det.xOK() & det.yOK()):
			det.switchCorners()

		coords_i = []
		#x_A
		coords_i.append(orig.x_A if (orig.x_A > det.x_A) else det.x_A)
		#y_A
		coords_i.append(det.y_A if (orig.y_A > det.y_A) else det.y_A)
		#x_B
		coords_i.append(det.x_B if (orig.x_B > det.x_B) else orig.x_B)
		#y_B
		coords_i.append(orig.y_B if (orig.y_B > det.y_B) else det.y_B)


		intersect = Rectangle(coords_i)
		if not (intersect.xOK() & intersect.yOK()):
			coords_i = [0,0,0,0]
			intersect.setCoords(coords_i)

		print intersect.getArea(), ", ", orig.getArea(), ", ", det.getArea()
		err += (orig.getArea() + det.getArea() - 3*intersect.getArea())
		
	print "Err: ", err
	print "Coords: ", len(coords_d)
	return err/len(coords_d)

if __name__ == '__main__':
	count()
