$(document).ready(function(){

   $("#dev-table-filter").keypress(  function(e) {
      search()
   })

   $(document).on( 'click', '#goodA', function() {
      aid = $(this).attr("name")
      upvoteAnswer(aid, true)
      setTimeout(function(){ 
         showAnswer()
      }, 50);
   })
   // $(document).on( 'click', '.tags', function() {
   //    alert('c1')
   //    $(this).parent.remove()
   //    alert('c2')
   // })
   $(document).on( 'click', '#badA', function() {
      aid = $(this).attr("name")
      upvoteAnswer(aid, false)
      setTimeout(function(){ 
         showAnswer()
      }, 50);
   })

   $('#clearTag').click(function(e){
      deleteAllTags()
      search()
   })
   $("#goodQ").click( function(e) {
      upvoteQuestion(true)
      key = $('#realQuestionID').text()
      setTimeout(function(){ 
         getQuestion(key)
      }, 50);
      

   })   
   $("#badQ").click(function(e) {
      upvoteQuestion(false)
      key = $('#realQuestionID').text()
      setTimeout(function(){ 
         getQuestion(key)
      }, 50);
      
   })  
   
   $("#addTag").click( function(e) {
      addTag()
      search()
   })
   
   $("#logout").click( function(e) {
      logout()
   })

   $('#back_button').click(
       function(){
         window.location.href='/searchOK'
       }
   )
   
   $("#answer_submit").click(
   function() {
      submitAnswer()
      showAnswer()
   })

   $(document).on( 'click', 'a.kevin', function() {
      var key = $(this).attr("id")
      getQuestion(key)
      setTimeout(function(){ 
         showAnswer()
      }, 50);
   })
   
   $('#showAnswer').hover( function() {
      showAnswer()
   })

   $(document).on("contextmenu",function(){
      return false;
   }); 
   

   $(document).bind('keydown', function(e) {
       if(e.ctrlKey && (e.which == 80)) {
       e.preventDefault();
       return false;
       }
   });


   $(document).bind('keydown', function(e) {
       if(e.ctrlKey && (e.which == 83)) {
       e.preventDefault();
       return false;
       }
   });
   document.onkeydown = function(e) {
       if(event.keyCode == 123) {
       return false;
       }
       if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)){
       return false;
       }
       if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)){
       return false;
       }
       if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)){
       return false;
       }
   }
})

////////////////////////////////////////////////////////FUNCTIONS///////////////////////////////////
function submitAnswer(){
   var body = $('#textarea').val()
       
      $.ajax({
         url: '/questions/' + $('#realQuestionID').text() + '/answers/add',
         type: 'POST',
               contentType:"application/json",
         dataType:"json",
         data: JSON.stringify({'body': body }),
         success: function (data){
                     stat = data['status'].toString()
                  
                     if(stat== "error"){
                        alert("Please Login to Answer Questions")
                     }else{
                        $('#textarea').val("")
                     }
         },
         error: function(err){
            alert("ERROR OCCURED WHILE PUTTING USER " + err)
         }
      })
}
function upvoteQuestion(bool){
   me = $('#realQuestionID').text()
      $.ajax({
         url: '/questions/' + $('#realQuestionID').text() + '/upvote',
         type: 'POST',
         contentType:"application/json",
         dataType:"json",
         data: JSON.stringify({'upvote': bool}),
         success: function (data){
            stat = data['status'].toString()
            if( stat == 'error'){
               alert('Please login to upvote/downvote')
            }
            

         },
         error: function(err){
            alert("ERROR OCCURED WHILE ADDING USER " + err)
         }
      })
}
function upvoteAnswer(aid, bool){
   
      $.ajax({
         url: '/answers/' + aid.toString() + '/upvote',
         type: 'POST',
         contentType:"application/json",
         dataType:"json",
         data: JSON.stringify({'upvote': bool}),
         success: function (data){
            stat = data['status'].toString()
            if( stat == 'error'){
               alert('Please login to upvote/downvote answer')
            }

         },
         error: function(err){
            alert("ERROR OCCURED WHILE ADDING USER " + err)
         }
      })
}

function showAnswer(){
   var key = $('#realQuestionID').text()
   $.ajax({
      url: '/questions/' + key.toString() +'/answers',
      type: 'GET',
      dataType:"html",
      success: function (data){
                  var data = JSON.parse(data);
                  $('#showAnswer').hide()
                  $('#textarea').show()
                  $('#answer_submit').show()
                  var myNode = document.getElementById("answerTable");
                  var fc = myNode.children[0];
                  while( fc ) {
                     myNode.removeChild( fc );
                     fc = myNode.firstChild;
                  }
                  
                  $.each(data['answers'],function(index,value){ 
                     
                     myvar =  '<br><br><div class="input" >' + 
                                 '<span >' +   value['body'] + '</span><br>' +
                                 '<div class="thumby" style="float:right">'+ 
                                    '<i id="goodA" class="fa fa-thumbs-up" name="' + value['id'].toString() + '"></i>' + 
                                    '<span style="font-size: 20px"> ' + value['score'] + " </span>"+
                                    '<i id="badA" class="fa fa-thumbs-down" name="'+ value['id'].toString() + '"></i>'  +
                                 '</div>' +
                              '</div>'
                        $('#answerTable').prepend(myvar)
                  });
      },
      error: function(err){
         
      }
   })
}

function getQuestion(key){
   $.ajax({
      url: '/questions/' + key.toString(),
      type: 'GET',
      dataType:"html",
      success: function (data){
                  var data = JSON.parse(data);
                  $('#realQuestionID').text(key) //hidden quention id 
                  $('#question_title').html(data['question']['title'])
                  $('#question_body').html(data['question']['body'])
                  $('#actual_body').show()
                  $('#dev-table').hide()
                  $('#searchMe').hide()
                  $('#textarea').hide()
                  $('#answer_submit').hide()
                  $('#showAnswer').show()
                  $('#voteCount').text(data['question']['score'])
                  var myNode = document.getElementById("answerTable");
                  var fc = myNode.children[0];
                  while( fc ) {
                     myNode.removeChild( fc );
                     fc = myNode.firstChild;
                  }
      },
      error: function(err){
         
      }
   })
}

function search(){
   $.ajax({
      url: '/search',
      type: 'POST',
      contentType:"application/json",
      dataType:"json",
      data: JSON.stringify({'q': $('#dev-table-filter').val(), 'tags': getAllTags() }),
      success: function (data){
                // data = JSON.parse(data)
                var myNode = document.getElementById("dev-table");
                var fc = myNode.children[1];
                while( fc ) {
                    myNode.removeChild( fc );
                    fc = myNode.firstChild;
                }
                var myvar = '<thead id=\'addHead\'> <tr> <th>    <a id=\'sortId\'>#</a></th> <th>    <a id=\'sortTitle\'>Questions</a>    </th> <th>    <a id=\'sortUser\'>User</a>  </th> <th>    <a id=\'sortDate\'>Date</a>         </th>  </tr></thead>';
                $( "#dev-table" ).append( myvar )
                myvar = '<tbody id=\'queryInfo\'></tbody>'
                $( "#dev-table" ).append( myvar )
                
                var i = 0
                $.each(data['questions'],function(index,value){ 
                    i+=1
                    myvar = '<tr>'+
                            '<th>' + i + '</th>'+
                            '<th>' + '<a class="kevin" id="' + value['id'].toString() + '">'+ value['title'] + '</a>' + '</th>' +
                            '<th>' + '[' + value['tags'].join(', ')+  ']</th>'+
                            '<th>' + value['timestamp'] + '</th>  '+
                            '</tr>';
                    
                        $('#queryInfo').append(myvar)
                    
                });
 
      },
      error: function(err){
         alert("ERROR OCCURED WHILE PUTTING USER " + err)
      }
   })
}
function logout(){
   $.ajax({
      url: '/logout',
      type: 'POST',
      contentType:"application/json",
      dataType:"json",
      data: JSON.stringify({}),
      success: function (data){
         
         window.location.href='/login'
      },
      error: function(err){
         alert("ERROR OCCURED WHILE ADDING USER " + err)
      }
   })
}


function addTag(){
   tag = $(".tag_box").val()
   if(tag.length == 0){
      alert("Tags cannot be empty")
   }else{
      ele = "<span class='tags'> " + tag  + "</span> &nbsp;"
      $("#tagTable").append(ele)
      $(".tag_box").val("") 
   }
}

function deleteAllTags(){
   var myNode = document.getElementById("tagTable");
   var fc = myNode.children[0];
   while( fc ) {
      myNode.removeChild( fc );
      fc = myNode.firstChild;
   }
}



function getAllTags(){
   tags = $(".tags")
   tagArr = []
   $.each(tags, function( i, value ) {
      tagArr.push(value.innerHTML.toString().trim() )
      });
   return tagArr
}
