import argparse, json

from os.path import abspath
from os.path import isfile
from indexer import index
from query import search

def main():
	parser = argparse.ArgumentParser()

	# Currently only optional argument support (later add optional arguments using subparsers)
	parser.add_argument("-f", "--filename", help="you want to index a new file.")
	parser.add_argument("-st", "--searchtags", help="search for a file based on tags", action="store_true")
	parser.add_argument("-sd", "--searchdescription", help="search for a file based on its description", action="store_true")
	parser.add_argument("-sn", "--searchname", help="search for a file based on its name", action="store_true")
	args = parser.parse_args()


	# if a file name is provided then index this file
	if args.filename:
		name = args.filename
		if isfile(name) == False:
			print 'Please give a file to index. Not anything else !!'
			return

		try:
			path = abspath(name)
			tags = raw_input("Tags [separated by a space]: ")
			desc = raw_input("Description [short description]: ")
		except KeyboardInterrupt:
			print '\nGracefully Exiting...'
			return

		doc = {
			"filename": name,
			"filepath": path,
			"tags": tags,
			"description": desc
		}
		index(doc)


	# if search on tags requested
	if args.searchtags:
		try:
			tags = raw_input('tags to be searched [space separated]: ')
		except KeyboardInterrupt:
			print '\nGracefully Exiting...'
			return

		search('tags:' + tags)


	# if search on description requested
	if args.searchdescription:
		try:
			desc = raw_input('rough description of file: ')
		except KeyboardInterrupt:
			print '\nGracefully Exiting...'
			return

		search('description:' + desc)


	# if search on name requested
	if args.searchname:
		try:
			name = raw_input('filename to be searched: ')
		except KeyboardInterrupt:
			print '\nGracefully Exiting...'
			return

		search('filename:' + name)


if __name__ == '__main__':
	main()
