from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
from negotiator import Negotiator

class MyConnection(RequestsHttpConnection):
    def __init__(self,*args, **kwargs):
        proxies = kwargs.pop('proxies', {})
        super(MyConnection, self).__init__(*args, **kwargs)
        self.session.proxies = proxies


negotiator = Negotiator()
answers = negotiator.get_es_data()

es = Elasticsearch(
    [answers['host']],
    connection_class=MyConnection,
    http_auth=(answers['username'], answers['password']),
    proxies={'http': answers['proxy']})
print('Connecting...')
if not es.ping():
    raise ValueError("Connection Failed")
print(es.cat.indices(v=True))
