curl -X DELETE "http://localhost:9200/tagz"

curl -X PUT "http://localhost:9200/tagz" -d '
{
    "mappings" : {
        "files" : {
            "properties" : {
                "path" : {
                    "type" : "string",
                    "index" : "not_analyzed" 
                }
            }
        }
    }

}
'
