import math
class Triangle:
	def __init__(self, a, b, c, p, h, v, m):
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)
		self.p = int(p)
		self.h = int(h)
		self.v = int(v)
		self.m = int(m)
	
	def __init__(self, a, b, c):
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)
		self.p = self.get_p()
		self.h = self.get_h()
		self.v = self.avr()
		self.m = self.max()
	def perim(self):
		return (self.a + self.b + self.c)
	
	def min(self):
		arr = [self.a, self.b, self.c]
		arr.sort()
		sup = arr[0]
		return sup
		
	def avr(self):
		arr = [self.a, self.b, self.c]
		arr.sort()
		sup = arr[1]
		return sup
		
	def max(self):
		arr = [self.a, self.b, self.c]
		arr.sort()
		sup = arr[2]
		return sup
	
	def get_p(self):
		p = (self.a + self.b+self.c)/2
		return p
	
	def get_h(self):
		h = ((2/v) *sqrt((self.get_p() - self.a)*(self.get_p() - self.b)*(self.get_p() - self.c)))
		return h
		
	def get_s(self):
		s = 0.5 * self.max() * self.get_h()
		return s
		
tra = Triangle(input('Enter a: '), input('Enter b: '), input("Enter c: "))
print('Perimeter: ' + str(tra.perim()))
tra.min()
tra.max()
print('Square: ' + tr.get_s)
