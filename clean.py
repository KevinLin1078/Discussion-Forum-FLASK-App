from flask import Flask 
import pymongo 
from pymongo import MongoClient
from bson.objectid import ObjectId

def clearMe():
   client = MongoClient('130.245.168.89', 27017)
   db = client['stack']         #    use wp2

   userTable = db['user'] 
   answerTable = db['answer']
   questionTable = db['question']
   ipTable = db['ip']
   upvoteTable = db['upvote']
   mediaTable = db['mediaID']

   userTable.drop()
   answerTable.drop()
   questionTable.drop()
   ipTable.drop() 
   upvoteTable.drop()
   mediaTable.drop()

   userTable = db['user'] 
   answerTable = db['answer']
   questionTable = db['question']
   ipTable = db['ip']
   upvoteTable = db['upvote']
   mediaTable = db['mediaID']


   userTable.insert({})
   answerTable.insert({})
   questionTable.insert({})
   ipTable.insert({})
   upvoteTable.insert({})
   mediaTable.insert({})

   userTable.delete_many({})
   answerTable.delete_many({})
   questionTable.delete_many({})
   ipTable.delete_many({})
   upvoteTable.delete_many({})
   mediaTable.delete_many({})
   print('UPDATED DATA')
   # questionTable.create_index([('title', pymongo.TEXT),('body', pymongo.TEXT )], name='search_index', default_language='none')
   
   # from datetime import datetime
   # from elasticsearch import Elasticsearch
   # from elasticsearch_dsl import Search
   # es = Elasticsearch([{'host': '130.245.170.76', 'port': 9200}])

   # es.indices.delete(index='test-index', ignore=[400, 404])
   print 'de'

def index():
   client = MongoClient('130.245.168.89', 27017)
   db = client['stack']         #    use wp2
   questionTable = db['question']

   question.insert({'title':"cat is stupid", 'body': 'dog is smart', 'tags': ['snake']})


def ppp():
   from datetime import datetime
   from elasticsearch import Elasticsearch
   from elasticsearch_dsl import Search
   es = Elasticsearch([{'host': '130.245.170.76', 'port': 9200}])

   es.indices.delete(index='questions', ignore=[400, 404])
   print 'de'
   doc = {
      'title': 'New15',
      'body': 'Elasticsearch: cool. bonsai cool.',
      'timestamp': datetime.now(),
      'tags': ['231', '23', '1232'],
      'media': ['mm','123'],
      'accepted_answer_id' :123
   }
   
   timestamp = datetime.now()
   # es.index(index="question", doc_type='place', id='123', body=doc)
   '''
   must_not ={  "should":[] ,"must": [  { "range": { "timestamp": { "lte": timestamp }}}], 'must_not': [] }
   must_not['should'].append(   {"match" : {"title": "New15" }}    )
   must_not['should'].append(   {"match" : {"body": "this cool is 123" }} )
   
   must_not['must'].append({ "exists": {"field": "accepted_answer_id" }}   ) 
   
   tags= ['231', '23']
   for item in tags:
		temp = {"terms" : {"tags": [item] } } 
		must_not['must'].append(temp)
   sort_by = 'timestamp'

   body ={  
            "sort" : [{ sort_by : {"order" : "desc"}}],
            "from" : 0, "size" : 25,
            "query" : {
               "constant_score" : {
                  "filter" : { 
                     "bool" : must_not,
                  }
               }
            }
         }

   
   res = es.search(index="question", body=body)
   for q in res['hits']['hits']:
      temp = {    
               'id': str(q['_id']),
               'title':q["_source"]['title'],
               'body': q["_source"]['body'],
               'tags': q["_source"]['tags'],
               'answer_count': 0,
               'media': q["_source"]['media'],
               # 'accepted_answer_id': q["_source"]['accepted_answer_id'] ,
               # 'user':q["_source"]['user'],
               'timestamp': q["_source"]['timestamp'],
               # 'score': q["_source"]['score'],
               # "view_count": q["_source"]['view_count']
            }
      print( q['_source'])
      '''

# clearMe()
# ppp()
# def connectM():
#    client = MongoClient('130.245.170.76', 27017)
#    db = client['stack']  


# query = "SELECT count(*) FROM imgs WHERE fileID = '" + 'DR5SW9DWY8GUXCEI4EKNW130YGCK3XAQF9JOA41X' + "';"
# row = cassSession.execute(query)[0].count

# print(row)



# res = es.index(index="test-index", doc_type='tweet', id='123', body=doc)
# print(res['result'])


# res = es.get(index="test-index", doc_type='tweet', id='123')
   # # print(res['_source'])