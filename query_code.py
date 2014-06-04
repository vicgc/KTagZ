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

	for i in range(0, len(lst)):
		print json.dumps( (lst[i])['_source'], sort_keys=True, indent=4, separators=(',', ': ') )

