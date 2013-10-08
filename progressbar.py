#!/usr/bin/env python
#
#  Corey Goldberg - 2010
#  ascii command-line progress bar with percentage and elapsed time display
#
#  updated by justasabc 2013.10

import sys
import time

if sys.platform.lower().startswith('win'):
	CARRAGE = '\r'
else:
	CARRAGE = chr(27) + '[A'

class ProgressBar:
    	def __init__(self, duration):
        	self.duration = duration
        	self.prog_bar = '[]'
        	self.fill_char = '='
        	self.width = 40
        	self.__update_amount(0)

    	def __str__(self):
        	return str(self.prog_bar)

    	def update_time(self, elapsed_secs):
		if elapsed_secs>self.duration:
			return
        	self.__update_amount((elapsed_secs / float(self.duration)) * 100.0)
        	self.prog_bar += ' {0}/{1}'.format(elapsed_secs, self.duration)
		# output prog_bar
		# \r move cursor to front
		# \n move cursor to next line
               	print self,CARRAGE

	def __update_amount(self, new_amount):
        	percent_done = int(round((new_amount / 100.0) * 100.0))
        	all_full = self.width - 2
        	num_hashes = int(round((percent_done / 100.0) * all_full))
        	self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        	pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
	        pct_string = '{0}%'.format(percent_done)
		self.prog_bar = self.prog_bar[0:pct_place] + pct_string + self.prog_bar[pct_place + len(pct_string):]
		return

    	def animate(self, secs):
        	for i in range(secs):
            		self.update_time(i + 1)
            		time.sleep(1) 
		return

def main():
	times = 5
	pb = ProgressBar(times)
	for i in range(times):
		pb.update_time(i+1)
		time.sleep(1)
	#pb.animate(5)

if __name__=="__main__":
	main()
