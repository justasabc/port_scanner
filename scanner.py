#!/usr/bin/env python
"""Python Port Scanner: scan given address for open ports."""
__app__ = "Python Port Scanner"
__version__ = "0.1.0"
__author__ = " Steve Gricci, justasabc"
__copyright__ = "(C) 2011-2014 Steve Gricci,justasabc. GNU GPL 3."
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
	parser = argparse.ArgumentParser(description='Python Port Scanner',epilog="Thank you for your using this application.If you find any bugs,please contact me at zunlin1234@gmail.com")
	parser.add_argument('-v','--version', action='version', version='{0} {1}'.format(__app__,__version__),help="show program's version number and exit")
	#parser.add_argument('-H','--HELP', action='help', help='show this help message and exit')
	parser.add_argument("IP", action="store",type=str,help="set ip or ip-range to scan. eg: 1)localhost 2) 192.168.1.200  3) 192.168.200-202 4)192-193.168-170.1-2.200-202")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-c", "--console",action="store_true", help = "run application in console mode(default)" )
	group_mode.add_argument("-g", "--gui", action = "store_true", help="run application in gui mode(to be done in the future...)")

	parser.add_argument("-f", "--file",dest="FILE",action="store",type=str,help="save scan result to FILE")
	parser.add_argument("-p", "--progress-bar",dest="progress_bar",action="store_true",help="show progress bar while processing")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-w", "--well-known",dest="well_known",action="store_true", help = "scan port which is less than well-known port 1024 (default)" )
	group_mode.add_argument("-m", "--max-port",dest="max_port", action = "store_true", help="scan port which is less than max-port 65535(may be slow)")
	global args
	args = parser.parse_args()

def process_one(ip,maxport,filename,con,progress_bar):
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
	open_ports = {}
	if progress_bar:
		pb = ProgressBar(maxport)
		for i in range(maxport+1):
			pb.update_time(i)
			if(scan_port(ip, i)):
				# right justify for sorting
				open_ports[str(i).rjust(5, '0')] = con.get(i)
	else:
		for i in range(maxport+1):
			if(scan_port(ip, i)):
				# right justify for sorting
				open_ports[str(i).rjust(5, '0')] = con.get(i)

	for port in sorted(open_ports.iterkeys()):
		p5 = str(int(port)).rjust(5,' ')
		msg = ("Port ({0}): {1}".format( p5, open_ports[port]))
		lines = lines + msg + os.linesep
		print(msg)

	# save results to file
	if filename:
		with open(filename,'a') as f:
			f.write(lines)

def console_main():
	# Check that an IP/Hostname was sent
	usage()
	# get params
	IP = args.IP
	progress_bar = args.progress_bar
	maxport = WELL_KNOWN 
	if args.max_port:
		maxport = MAX_PORT
		# if use MAX_PORT, then show progress bar
		progress_bar = True
	filename = None
	if args.FILE and args.FILE.strip():
		filename = args.FILE.strip()
		if not inside('.',filename):
			sys.stderr.write("ERROR: file must be inside current folder"+os.linesep)
			sys.exit(1)
	# Load Configuration
	con = Config('ports.ini')

	parser = IPParser(IP)
	ips = parser.parse()
	if len(ips)<1:
		sys.stderr.write("ERROR: invaid ips"+os.linesep)
		sys.exit(1)

	for ip in ips:
		process_one(ip,maxport,filename,con,progress_bar)

if __name__ == '__main__':
	console_main()
