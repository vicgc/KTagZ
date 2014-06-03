import argparse
import os, json

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
	tags = raw_input("Tags [separate by space]: ")

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

print json.dumps(doc, sort_keys=True, indent=4, separators=(',', ': '))
