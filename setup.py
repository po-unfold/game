#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |
# |                        |
# | Do not edit this file  |
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
	with open("README.md", "r") as fh:
		long_description = fh.read()
except FileNotFoundError:
	long_description = """
	# Pushing_Outshoot_Unfold
	A game about a teen getting through quarantine in Covid.
	### Contributors
	- Cole, Harshini, Cassidy
	### Contact
	<po-unfold@colewilson.xyz>
	"""

options = {
	"name": "pushing_outshoot_unfold",
	"version": "0.1.1",
	"scripts": [],
	"entry_points": {'console_scripts': ['pou=pushing_outshoot_unfold.__main__:main']},
	"author": "Cole, Harshini, Cassidy",
	"author_email": "po-unfold@colewilson.xyz",
	"description": "A game about a teen getting through quarantine in Covid.",
	"long_description": long_description,
	"long_description_content_type": "text/markdown",
	"url": "https://github.com/po-unfold",
	"packages": setuptools.find_packages(),
	"install_requires": ['blessed', 'toml', 'replit'],
	"classifiers": ["Programming Language :: Python :: 3"],
	"python_requires": '>=3.6',
	"package_data": {"": ['sounds/*', 'days/*.toml', 'days2/*.toml', 'days3/*.toml'], },
	"license": "none",
	"keywords": '',
	"setup_requires": ['wheel'],
}

custom_options = {}

if __name__ == "__main__":
	setuptools.setup(**custom_options, **options)
