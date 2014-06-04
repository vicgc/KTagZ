from elasticsearch import Elasticsearch

es = Elasticsearch()
print es.get(index='tagz', doc_type='files')
