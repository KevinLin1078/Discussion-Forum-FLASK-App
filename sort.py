import pymongo 
from pymongo import MongoClient

client = MongoClient()

db = client.stack
userTable = db['user'] 
answerTable = db['answer']
aidTable = db['answer_id']
questionTable = db['question']
pidTable = db['pid']
ipTable = db['ip']



def getSortDate():
    questFilter =[]
    allQuestion = questionTable.find();
    
    for q in allQuestion:
        questFilter.append(q)
    questFilter.sort(key=lambda x: x['time'], reverse=True)
    return questFilter

def getSortUser():
    questFilter =[]
    allQuestion = questionTable.find();
    
    for q in allQuestion:
        questFilter.append(q)
    
    questFilter.sort(key=lambda x: x['username'], reverse=True)
    print(questFilter)
    return questFilter

def getSortTitle():
    questFilter =[]
    allQuestion = questionTable.find();
    
    for q in allQuestion:
        questFilter.append(q)
    
    questFilter.sort(key=lambda x: x['title'], reverse=True)
    print(questFilter)
    return questFilter

