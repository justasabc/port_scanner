#!/usr/bin/env python
"""Python Port Scanner: scan given address for open ports."""
__version__ = "0.1.0"
__author__ = "justasabc (zunlin1234@gmail.com)"
__copyright__ = "(C) 2013-2014 justasabc. GNU GPL 3."
__contributors__ = ['justasabc','Steve Gricci']

import sys
import os
import argparse
# user defined
from utils import *
from settings import *
from config import Config
from ipparser import IPParser
from progressbar import ProgressBar

args = None

# argparse
def usage(): 
	parser = argparse.ArgumentParser(description='Python Port Scanner')
	parser.add_argument("IP", action="store",type=str,help="set ip or ip-range to scan. eg: 1)localhost 2) 192.168.1.200  3) 192.168.200-202 4)192-193.168-170.1-2.200-202")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-c", "--console",action="store_true", help = "run application in console mode(default)" )
	group_mode.add_argument("-g", "--gui", action = "store_true", help="run application in gui mode(to be done in the future...)")

	parser.add_argument("-f", "--FILE",dest="FILE",action="store",type=str,help="save scan result to FILE")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-w", "--well-known",dest="well_known",action="store_true", help = "scan port which is less than well-known port 1024 (default)" )
	group_mode.add_argument("-m", "--max-port",dest="max_port", action = "store_true", help="scan port which is less than max-port 65535(may be slow)")
	global args
	args = parser.parse_args()

def process_one(ip,maxport,filename,con):
	"""
	process give ip
	"""
	lines = ""
	# Check if the host is up first
	if (is_host_up(ip) == False):
		msg = ("DOWN: {0} is down").format(ip)
		lines = lines + msg + os.linesep
		print(msg)
		return	

	msg = ('Starting scan on host: {0}'.format(ip))
	lines = lines + msg + os.linesep
	print(msg)
	pb = ProgressBar(maxport)
	open_ports = {}
	for i in range(maxport+1):
		pb.update_time(i)
		if(scan_port(ip, i)):
			# right justify for sorting
			open_ports[str(i).rjust(5, '0')] = con.get(i)

	for port in sorted(open_ports.iterkeys()):
		p5 = str(int(port)).rjust(5,' ')
		msg = ("Port ({0}): {1}".format( p5, open_ports[port]))
		lines = lines + msg + os.linesep
		print(msg)

	if filename:
		with open(filename,'a') as f:
			f.write(lines)

def console_main():
	# Check that an IP/Hostname was sent
	usage()
	# get params
	maxport = WELL_KNOWN 
	IP = args.IP
	if args.max_port:
		maxport = MAX_PORT
	filename = None
	if args.FILE and args.FILE.strip():
		filename = args.FILE.strip()
	# Load Configuration
	con = Config('ports.ini')

	parser = IPParser(IP)
	ips = parser.parse()
	if len(ips)<1:
		sys.stderr.write("ERROR: invaid ips"+os.linesep)
		sys.exit(1)

	for ip in ips:
		process_one(ip,maxport,filename,con)

if __name__ == '__main__':
	console_main()
