import username as username
from flask import Flask, request
from datetime import datetime

app = Flask (__name__)

@app.route("/")
def home():
        return """
            <html><body> 
             <form action="/pogi">
             What's your name? <input type='text' name='username'><br>
              What's your characteristic? <input type='text' name='char'><br> 
              <input type='submit' value='Continue'>
               </form> </body></html>
               """
@app.route('/pogi')
def greet():
    username = request.args.get("username","World")
    char =  request.args ['char']
    if char =='':
                msg= 'you did not enter your characteristc'
    else:
         msg = username + ' is ' + char

    return """
                  <html><body>
                   <h2>Hello, {0}!</h2> 
                   {1}
                    </body></html> 
                   """.format(username, msg)



app.run(host="localhost", debug=True)
