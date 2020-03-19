# from elasticsearch import Elasticsearch
#
# es = Elasticsearch('http://localhost:9200')
#
# index = "post"
# # res = es.index(index=index, doc_type=index, body={'hello':'ok'}, id=1)
# res = es.get(index=index, doc_type=index, id=18)
# print(res['_source'])
# import cr
import os

a = os.environ.get('b')
print(a)
