from setuptools import setup

setup(
	name = "TagZ",
	version = "0.1",
	description = "A command line file-tagger for linux",
	author = "Khirod Kant Naik",
	author_email = "khirod234@gmail.com",
	url = "kkantnaik.blogspot.in",
	py_modules = ["client", "query"],
	scripts = ["tagz"],
)
