#!/usr/bin/env python

class PortConfig:
	"""
	config for all common ports:
	port:description
	"""
	def __init__(self, filename):
		self.filename = filename
		self.buffers = open(filename).readlines()
		self.mem = {} # port:description
		self.__parse()
		return

	def get(self, config_name):
		return self.mem.get(str(config_name),'unknown')

	def total(self):
		return len(self.mem)

	def __parse(self):
		for line in self.buffers:
			sp = line.split(':')
			sp[0] = str(sp[0])
			self.mem[sp[0]] = sp[1].strip()
		return

def main():
	con = PortConfig('ports.ini')
	print(con.total()) # 896    ???
	print(con.get(22))
	print(con.get(80))

if __name__=="__main__":
	main()
