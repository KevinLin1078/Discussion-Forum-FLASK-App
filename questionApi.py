@threading
def upvoteQuestionTrue(result, user, pid, realUser):
   if result == None:
      upvoteTable.insert({'username': user, 'pid': pid, 'vote': 1})
      updateQuestionScore(pid, realUser, 1, 1)
   elif result['vote'] ==  1:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': 0} } )
      updateQuestionScore(pid, realUser, -1,-1)	
   elif result['vote'] ==  0:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': 1} } )
      updateQuestionScore(pid, realUser, 1, 1)
   elif result['vote'] == -1:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': 1} } )
      updateQuestionScore(pid, realUser, 2, 1)


@threading
def upvoteQuestionFalse(result, user, pid, realUser):
   if result == None:
      upvoteTable.insert({'username': user, 'pid': pid, 'vote': -1})
      updateQuestionScore(pid, realUser, -1, -1)
   elif result['vote'] ==  -1:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': 0} } )			
      updateQuestionScore(pid, realUser, 1, 1)	
   elif result['vote'] ==  0:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': -1} } )
      updateQuestionScore(pid, realUser, -1, -1)
   elif result['vote'] == 1:
      upvoteTable.update_one({'username':user, 'pid': pid} , { "$set": {'vote': -1} } )
      updateQuestionScore(pid, realUser, -2, -1)



@threading
def upvoteAnswerTrue(result, user, aid, realUser):
   if result == None:
      upvoteTable.insert({'username': user, 'aid': aid, 'vote': 1})
      updateAnswerScore(aid, realUser, 1,1)	
   elif result['vote'] ==  1:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': 0} } )
      updateAnswerScore(aid, realUser, -1,-1)	
   elif result['vote'] ==  0:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': 1} } )
      updateAnswerScore(aid, realUser, 1, 1)
   elif result['vote'] == -1:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': 1} } )
      updateAnswerScore(aid, realUser, 2, 1)


@threading
def upvoteAnswerFalse(result, user, aid, realUser):
   if result == None:
      upvoteTable.insert({'username': user, 'aid': aid, 'vote': -1})
      updateAnswerScore(aid, realUser, -1, -1)
   elif result['vote'] ==  -1:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': 0} } )			
      updateAnswerScore(aid, realUser, 1, 1)	
   elif result['vote'] ==  0:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': -1} } )
      updateAnswerScore(aid, realUser, -1, -1)
   elif result['vote'] == 1:
      upvoteTable.update_one({'username':user, 'aid': aid} , { "$set": {'vote': -1} } )
      updateAnswerScore(aid, realUser, -2, -1)

@threading
def acceptAnswer(aid, pid):
   answerTable.update_one({'_id': aid}, { "$set": {'is_accepted': True} })
	questionTable.update_one({'_id': pid }, { "$set": {'accepted_answer_id': IDD}} )