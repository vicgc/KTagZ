from distutils.core import setup

setup(
	name = "Ghanta Singh",
	version = "0.1",
	description = "A command line file-tagger for linux",
	author = "Khirod Kant Naik",
	author_email = "khirod234@gmail.com",
	url = "kkantnaik.blogspot.in",
	py_modules = ["tagz.py", "query_code.py"],
	scripts = ["tagz"],
)
