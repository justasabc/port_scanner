"""
file: version.py
This file contains version info of this app.
"""

__all__ = ['__app__','__version__','version','app_name']

__app__ = "Python Port Scanner"
__version__ = "0.1.0"
__author__ = " Steve Gricci, justasabc"
__copyright__ = "(C) 2011-2014 Steve Gricci,justasabc. GNU GPL 3."
__contributors__ = ['justasabc','Steve Gricci']

def app_name():
	return __app__

def version():
	return __version__

