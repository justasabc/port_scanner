#!/usr/bin/env python

class IPParser:
	"""
	class to parse IPs
	for example:
	localhost --->127.0.0.1
	192.168.1.200
	192.168.1.200-202
	192-193.168-170.1-2.200-202
	"""
	local_key = 'localhost'
	local_value = '127.0.0.1'

	def __init__(self, ip_str):
		self.ip_str = ip_str.strip()
		#self.ipmatch = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
		return

	def parse(self):
		if self.ip_str == self.local_key:
			return [self.local_value]
		parts = self.ip_str.split('.')
		#print(parts)
		if len(parts) != 4:
			return []
		ar = self.__get_range(parts[0])
		br = self.__get_range(parts[1])
		cr = self.__get_range(parts[2])
		dr = self.__get_range(parts[3])
		#print(ar,br,cr,dr)
		return [self.__format_ip(a,b,c,d) for a in ar for b in br for c in cr for d in dr]
	
	def __get_range(self,str_range):
		"""
		get range from str
		eg: 192-195 / 192- / 192
		return [192,193,194,195]
		"""
		sp = str_range.split('-')
		if len(sp)==2 and self.__ip_in_range(sp[0]) and self.__ip_in_range(sp[1]):
			ia = int(sp[0])
			ib = int(sp[1])
			return [str(x) for x in range(ia,ib+1)]
		elif len(sp)==1 and self.__ip_in_range(sp[0]):
			return [sp[0]]
		else:
			return []
		
	def __ip_in_range(self,value):
		"""
		check if value is in ip range
		"""
		try:
			iv = int(value)
			return 0 <= iv < 256
		except:
			return False

	def __format_ip(self,a,b,c,d):
		"""
		format ip from a b c d
		"""
		return "{0}.{1}.{2}.{3}".format(a,b,c,d)


def main():
	print('-'*30)
	ip_str = "localhost"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)
	print('-'*30)
	ip_str = "192.168.1.200"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)
	print('-'*30)
	ip_str = "192.168.1.200-202"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)
	print('-'*30)
	ip_str = "192-193.168-169.1-2.200-201"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)
	print('-'*30)
	ip_str = "a-b.168-170.1-2.200-202"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)
	print('-'*30)
	ip_str = "192-193.168-170.1-2.a-b"
	print(ip_str)
	parser = IPParser(ip_str)
	ips = parser.parse()
	print(len(ips))
	print(ips)

if __name__ =="__main__":
	main()
