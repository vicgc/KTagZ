# Experimental File

import argparse
import os, json
from elasticsearch import Elasticsearch
import uuid

def main():
	parser = argparse.ArgumentParser()

	# File to be indexed is a positional argument
	parser.add_argument("file_name", help="file to be indexed")

	# Currently only optional argument support (later add optional arguments using subparsers)
	parser.add_argument("-t","--tags", help="Adds tags to file", action="store_true")
	parser.add_argument("-d", "--desc", help="Adds description to a file", action="store_true")
	args = parser.parse_args()

	tags = ""
	desc = ""

	if args.tags:
		tags = raw_input("Tags [separated by a space]: ")

	if args.desc:
		desc = raw_input("Description [short description]: ")

	
	name = args.file_name
	tags = tags.split(' ')
	path = os.getcwd() + '/' + args.file_name

	doc = {
		"file": name,
		"path": path,
		"tags": tags,
		"description": desc
	}

	unique_id = str(uuid.uuid4())

	try:
		es = Elasticsearch()
		es.index(index='tagz', doc_type='files', id=unique_id, body=doc)
	except:
		print 'Oops!. Encountered an error'

if __name__ == '__main__':
	main()
