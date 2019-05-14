from flask import Blueprint, render_template, abort, Flask, request, url_for, json, redirect, Response, session, g
from werkzeug.security import check_password_hash, generate_password_hash
import  datetime, json
from flask_mail import Mail
from flask_mail import Message
import pymongo 
from pymongo import MongoClient
import time
from bson.objectid import ObjectId

client = MongoClient('130.245.168.89', 27017)
bp = Blueprint('question', __name__, template_folder='templates')

db = client.stack
userTable = db['user'] 
answerTable = db['answer']
questionTable = db['question']
ipTable = db['ip']
upvoteTable = db['upvote']
mediaTable = db['mediaID']


@bp.app_errorhandler(404)
def handle404(error):
    return responseOK({'status': 'OK'})
@bp.app_errorhandler(500)
def handle505(error):
    return responseOK({'status': 'OK'})



@bp.route('/questions/add', methods=["POST", "GET"])
def addQuestion():
    if request.method == "GET":
        return render_template('addQuestion.html')
    if(request.method == 'POST'):
        
        pid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40))
        
        return responseOK({ 'status': 'OK', 'id':"3uWiRhERjvdfggcfxdzaz"}) 

@bp.route('/questions/<IDD>', methods=[ "GET", 'DELETE'])
def getQuestion(IDD):
    pid = ObjectId(str(IDD))
    if request.method == 'GET':
        #print("=========================QUESTION/ID====GET===============================")
        result = questionTable.find_one({"_id": pid})

        if( result == None):
            print("QUESTION ID DOESNT EXIST")
            print(request.remote_addr)
            return responseOK({'status':'error', 'error': 'id doesnt exist'})
        ip = request.remote_addr
        ip = str(ip)
        plus = 0

        name = request.cookies.get('token')
        
        if not name:
            if ipTable.find_one({'ip':ip , 'pid':pid}) == None:
                ipTable.insert({'ip':ip, 'pid': pid})
                plus = 1
        else:
            if ipTable.find_one({'ipN': name , 'pid':pid} ) == None:
                ipTable.insert({'ipN' : name, 'pid': pid})
                plus = 1
        
        count = result['view_count']
        questionTable.update_one({'_id':pid}, { "$set": {'view_count': count + plus}} )
        result = questionTable.find_one({'_id':pid})
        score = result['score']
        view_count = result['view_count']
        answer_count = result['answer_count']
        media = result['media']
        tags = result['tags']
        title = result['title']
        body = result['body']
        pid = str(result['_id'])
        timestamp = result['timestamp']
        
        user = result['user']['username']
        reputation = userTable.find_one({'username':user})
        reputation = reputation['reputation']

        question =  {   'status':'OK',
                            "question": {
                                    "score": score,
                                    "view_count": view_count,
                                    "answer_count": 0,
                                    "media": media,
                                    "tags": tags,
                                    "accepted_answer_id": result['accepted_answer_id'],
                                    "title": title,
                                    "body": body,
                                    "id": pid,
                                    "timestamp": timestamp,
                                    "user": {
                                                'username': user,
                                                'reputation' :reputation
                                            }
                                    },
                            "id": pid,  
                        }
        return responseOK(question)

    elif request.method == 'DELETE':
        print("=========================QUESTION/ID====DELETE===============================")
        name = request.cookies.get('token')
        
        if not name:
            print('Add Question Wrong SESSION')     
            return responseNO({'status': 'error', 'error': 'Wrong user session'})
        else:
            pid = ObjectId(str(IDD))
            result = questionTable.find_one({'_id':pid})
            if( result == None):
                print('FAILED DELTED, invalid QUESTIONS ID')
                return responseNO({'status':'error','error':'Question does not exist'})

            username = result['user']['username']
            if name != username:
                print('FAILED DELTED, user is not original')
                return responseNO({'status':'error', 'error': 'Not orginal user'})
            else:
                print('SUCCESSFULLY DELTED, user is original')
                question_delete = questionTable.find_one({'_id': pid})
                allMedia = question_delete['media']
                for m in allMedia:
                    query = "DELETE FROM imgs WHERE fileID = '" + m + "';"
                    print('=============', m)
                    row = cassSession.execute(query)
                
                answer_delete = answerTable.find({'pid': pid})
                for a in answer_delete:
                    ans_media = a['media']
                    for i in ans_media:
                        query = "DELETE FROM imgs WHERE fileID = '" + i + "';"
                        print('=============', m)
                        row = cassSession.execute(query)


                questionTable.delete_one({'_id': pid})
                answerTable.delete_many({'pid': pid})
                ipTable.delete_many({'pid': pid})
                return responseOK({'status': 'OK'})
                

@bp.route('/questions/<IDD>/answers/add', methods=["POST", "GET"])
def addAnswer(IDD):
    if request.method == 'POST':
        name = request.cookies.get('token')
        if not name:
            print("NO session answer")
            return responseNO({'status': 'error','error': 'not logged in'})
        return responseOK({'status': 'OK', 'id': 'Anfhrk33kgerlf3Dedfe'})

@bp.route('/questions/<IDD>/answers', methods=['GET'])
def getAnswers(IDD):
    if request.method == 'GET':
        answerReturn = {"status":"OK", 'answers': []}
        return responseOK(answerReturn)

@bp.route('/questions/<IDD>/upvote', methods=['POST'])
def upvoteQuestion(IDD):
    if request.method == 'POST':
        pid = str(IDD)
        name = request.cookies.get('token')
        if not name:
            return responseNO({'status': 'error','error': 'Please login to upvote question'})
        return responseOK({'status': 'OK'})

@bp.route('/answers/<IDD>/upvote', methods=['POST'])
def upvoteAnswer(IDD):
    if request.method == 'POST':
        aid = str(IDD)
        
        name = request.cookies.get('token')
        if not name:
            return responseNO({'status': 'error','error': 'Please login to upvote answer'})
        return responseOK({'status': 'OK'})

@bp.route('/answers/<IDD>/accept', methods=['POST'])
def acceptAnswer(IDD):
    if request.method == 'POST':
        name = request.cookies.get('token')
        if not name:
            return responseNO({'status': 'error','error': 'Please login to accept answer'})       
    
    return responseOK({'status': 'OK'})


@bp.route('/searchOK', methods=['GET'])
def searchOK():
    if request.method == 'GET':
        result = questionTable.find()
        login= 0
        if len(session) == 0:
            login = 0
        else:
            login = 1
        return render_template('questionTable.html', questionTable=result, login= login)

@bp.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':   
        answer = {'status' : 'OK', 'questions': []}
        return responseOK(answer)


def responseOK(stat):
    data = stat
    jsonData = json.dumps(data)
    respond = Response(jsonData,status=200, mimetype='application/json')
    return respond

def responseNO(stat):
    data = stat
    jsonData = json.dumps(data)
    respond = Response(jsonData,status=400, mimetype='application/json')
    return respond


