filter_package_names.py
rfc 2012

Purpose: Filter output from dpkg -l based on pattern

Example 1: print a list of installed packages

	dpkg -l | ./filter_package_names.py ii | less

Example 2: purge all configuration files of removed packages

	dpkg -l | ./filter_package_names.py rc | xargs sudo apt-get purge --assume-yes
