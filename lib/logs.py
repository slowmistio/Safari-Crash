#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from os.path import expanduser
from termcolor import colored
import os
import string
import sys
import subprocess
import linecache
import sys

HOME = expanduser('~')

class color:
		PURPLE = '\033[95m'
		CYAN = '\033[96m'
		DARKCYAN = '\033[36m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		END = '\033[0m'
		BLINK = '\033[5m'
		DIM = '\033[2m'
		HIDDEN = '\033[8m'
		MAGENTA = '\033[95m'
		LIGHT_MAGENTA = '\033[95m'


class Logs:
		def __init__(self):
				self.logfile = self.__set_logfile_name()

		def __set_logfile_name(self):
				filename = sys.argv[0]
				logfile = filename.replace('./', '').replace('.py', '')
				logfile += '_log'
				return logfile

def err(msg, prnt=True):
		p = '[%s] %s' % (colored('✘', 'red'), msg)
		if prnt:
			print p
		return p

def purple(msg):
		p = '{}{}{}'.format(color().LIGHT_MAGENTA, msg, color().END)
		return p

def good(msg, prnt=True):
		p = '[%s] %s' % (colored('+', 'green'), msg)
		if prnt:
			print p
		return p

def underline(msg):
		p = '{}{}{}'.format(color().UNDERLINE, msg, color().END)
		return p

def green(msg):
		p = colored(msg, 'green')
		return p

def yellow(msg):
		p = '{}{}{}'.format(color().YELLOW, msg, color().END)
		return p

def underline(msg):
		p =  color().UNDERLINE+msg+color().END
		return p

		
def bold(msg):
		p = '{}{}{}'.format(color().BOLD, msg, color().END)
		return p

def wrn(msg, prnt=True):
		p = '[%s] %s' % (colored('WARNING', 'red'), msg)
		if prnt:
			print p
		return p



def info(msg, prnt=True):
		info = '[INFO] %s' % msg
		if prnt:
			print info
		return info

def star(msg, color='magenta', pnt=True):
		p = '%s%s' %(colored('✶', color), msg)
		print p

def e(comm):
	subprocess.call(comm, shell = True)


def red(string):
		return colored(string, 'red')

def blue(string):
		return color().CYAN + string + color().END

def brackets(string, bracket=']', color='red'):
		if bracket == ']':
				return '%s%s%s' % (colored('[', color), string, colored(']', color))

def print_exception():
		exc_type, exc_obj, tb = sys.exc_info()
		f = tb.tb_frame
		lineno = tb.tb_lineno
		filename = f.f_code.co_filename
		linecache.checkcache(filename)
		line = linecache.getline(filename, lineno, f.f_globals)
		print '\n[{}][{}][{}] => {}): {}'.format(red('EXCEPTION'), filename.split('/')[-1], lineno, line.strip(), exc_obj)
