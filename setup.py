from setuptools import setup
from setuptools import find_packages

setup(
	name = "ktagz",
	packages = find_packages(),
	version = "0.1.0",
	description = "A command line file-tagger/file-search tool for linux",
	long_description = 'Basically it can help you with tagging files and then you can easily search files with a particular tag using text search.',
	author = "Khirod Kant Naik",
	author_email = "khirod234@gmail.com",
	url='https://github.com/shinigamiryuk/TagZ',
	scripts = ['bin/tagz'],
	install_requires=[
	"elasticsearch >= 1.0.0",
	]
)
