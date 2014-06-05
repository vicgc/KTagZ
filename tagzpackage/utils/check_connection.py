from elasticsearch import Elasticsearch

def check():
	try:
		es = Elasticsearch()
	except:
		return False

	return True
	
