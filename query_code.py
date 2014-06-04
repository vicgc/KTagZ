from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

doc = {
	"query": {
		"query_string": {
			"query": "github fuck readme tutorial"
		}
	}
}

res = es.search(index='tagz', doc_type='files', body=doc)
lst = (res['hits'])['hits']

for i in range(0, len(lst)):
	print json.dumps( (lst[i])['_source'], sort_keys=True, indent=4, separators=(',', ': ') )

