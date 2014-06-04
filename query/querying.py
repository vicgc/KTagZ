import json

def query(es):

	tags = raw_input("Enter tags to be searched [space separated]: ")
	doc = {
		"query": {
			"query_string": {
				"query": tags,
				"fields": ["tags"]
			}
		}
	}

	res = es.search(index='tagz', doc_type='files', body=doc)
	lst = (res['hits'])['hits']
	
	if len(lst):
		print 'Files containing the given tags are: \n=============================================='

	for i in range(0, len(lst)):
		ob = (lst[i])['_source']

		print '*  File Name: ' + ob['file']
		print '*  Description: ' + ob['description']
		print '*  File Path: ' + ob['path']
		print '*  File Tags: ' + str(ob['tags'])

		print '\n\n'		

