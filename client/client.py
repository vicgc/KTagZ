# Experimental File

import argparse
import os, json
from elasticsearch import Elasticsearch
import uuid
from query import querying as qr

def main():
	parser = argparse.ArgumentParser()
	es = Elasticsearch()

	# Currently only optional argument support (later add optional arguments using subparsers)
	parser.add_argument("-f", "--filename", help="you want to index a new file")
	parser.add_argument("-s", "--search", help="search a file", action="store_true")
	args = parser.parse_args()

	if args.filename:
		name = args.filename
		tags = (raw_input("Tags [separated by a space]: ")).split(' ')
		desc = (raw_input("Description [short description]: "))
		path = os.getcwd() + '/' + args.filename

		doc = {
			"file": name,
			"path": path,
			"tags": tags,
			"description": desc
		}

		unique_id = str(uuid.uuid4())
		es.index(index='tagz', doc_type='files', id=unique_id, body=doc)

	if args.search:
		qr.query(es)



if __name__ == '__main__':
	main()
