#!/usr/bin/env python

from socket import *
import sys
import os
import subprocess

# get platform first
WIN = 1
LINUX = 2
MAC = 3

def get_platform():
	"""
	get platform
	"""
	if sys.platform.startswith("win32"):
		return WIN
	elif sys.platform.startswith("linux"):
		return LINUX
	elif sys.platform.startswith("darwin"):
		return MAC
	else:
		return LINUX

PLATFORM = get_platform()
# get platform first

def is_host_up(ip):
	"""
	check if host is up
	"""
	if PLATFORM == WIN:
		pingstr="ping -n 1 -i 1 {0}".format(ip)
	else:
		pingstr="ping -c 1 -t 1 {0}".format(ip)
	ret = subprocess.call(pingstr, shell=True, stdout=open('/dev/null','w'), stderr=subprocess.STDOUT)
	if (ret == 0): # 0 means ping success
		return True
	return False

def scan_port(ip, port):
	"""
	scan a given ip and port
	return True if connect successfully, otherwise False
	"""
	setdefaulttimeout(.5)
	s = socket(AF_INET, SOCK_STREAM)
	# s.settimeout(.5)
	result = s.connect_ex((ip, port))
	s.close()
	if (result == 0):
		return True
	return False


def is_host_up2(ip):
	ret = subprocess.call("ping -c 1 -t 1 %s" % ip,
			shell=True, stdout=open('/dev/null','w'),
			stderr=subprocess.STDOUT)
	if (ret == 0): # 0 means ping success
		return True
	return False

def inside(dirname,filepath):
	"""
         check whether file exists in dir folder 
	 ./  ./1.txt
        """
	absdir = os.path.abspath(dirname)
	absfile = os.path.abspath(filepath)
	# make sure absdir2 end with '/'
	absdir2 = os.path.join(absdir,'')
	return absfile.startswith(absdir2)

def clear_screen():
	"""
	clear screen
	"""
	if PLATFORM == WIN:
        	os.system('cls')
    	elif PLATFORM == LINUX:
		os.system('clear')
	else:
		pass

def test():
	print("test platform")
	print(PLATFORM)
	ip = "192.168.1.200"
	print(is_host_up(ip))
	ip = "192.168.1.198"
	print(is_host_up(ip))

def main():
	test()

if __name__=="__main__":
	main()
