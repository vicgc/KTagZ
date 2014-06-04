from setuptools import setup
from setuptools import find_packages

setup(
	name = "tagz",
	packages = find_packages(),
	version = "0.1.0",
	description = "A command line file-tagger for linux",
	author = "Khirod Kant Naik",
	author_email = "khirod234@gmail.com",
	url='https://github.com/shinigamiryuk/TagZ',
	scripts = ['bin/tagz'],
	install_requires=[
	"elasticsearch >= 1.0.0",
	]
)
