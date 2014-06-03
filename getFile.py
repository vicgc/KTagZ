from elasticsearch import Elasticsearch 
import json

def getdocbyID(client, indexName, typeName, oid):
	res = client.get(index=indexName, doc_type=typeName, id=oid)
	print json.dumps(res['_source'], sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	es = Elasticsearch()	# ES client
	indexName = 'tagz'		# index-name
	typeName = 'files'		# type-name

	getdocbyID(es, indexName, typeName, 1)
	getdocbyID(es, indexName, typeName, 2)