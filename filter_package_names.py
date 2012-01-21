#! /usr/bin/env python

"""
filter_package_names.py
rfc 2012

Purpose: Filter output from dpkg -l based on pattern

Example 1: print a list of installed packages

	dpkg -l | ./filter_package_names.py ii | less

Example 2: purge all configuration files of removed packages

	dpkg -l | ./filter_package_names.py rc | xargs sudo apt-get purge --assume-yes
"""

import sys

def package_name(line):
	line = line.strip()
	line = line.split()
	return line[1]

def main():
	if len(sys.argv) != 2:
		print 'usage: pattern [e.g. ii]'
		sys.exit(1)
	pattern = sys.argv[1]

	for x in sys.stdin:
		if x.split()[0] != pattern:
			continue
		print package_name(x)

if __name__ == '__main__':
	main()
