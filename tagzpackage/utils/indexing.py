def indexDoc(es, idx, otype, oid, doc):
	try:
		res = es.index(index=idx, doc_type=otype, id=oid, body=doc)
		print 'Okay!! Indexed'
	except:
		print 'Encountered error while indexing. Is ElasticSearch instance running ?'
		
