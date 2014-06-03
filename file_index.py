from elasticsearch import Elasticsearch 

def indexDoc(client, indexName, typeName, oid, data):
	res = client.index(index=indexName, doc_type=typeName, id=oid, body=data)
	print (res['created'])


if __name__ == '__main__':
	es = Elasticsearch()	# ES client
	indexName = 'tagz'		# index-name
	typeName = 'files'		# type-name

	doc = {
		"name":	"xyz",
		"type":	"textfile",
		"path": "/home/khirod/xyz.cpp",
		"tags": ["programming", "dynamic-programming", "codeforces"],
		"description": "Just another codeforces problem. ;)"
	}

	indexDoc(es, indexName, typeName, 1, doc)

	doc = {
		"name":	"abc",
		"type":	"music",
		"path": "/home/khirod/abc.mp3",
		"tags": ["thrash", "metal", "live"],
		"description": "Ahh Love Dream Theater !!"
	}

	indexDoc(es, indexName, typeName, 2, doc)		