"""This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.
Methods
1. score_server - This function will serve the score. It will read the score from the scores
file and will return an HTML that will be as follows:
<html>
 <head>
 <title>Scores Game</title>
 </head>
 <body>
 <h1>The score is <div id="score">{SCORE}</div></h1>
 </body>
</html>
If the function will have a problem showing the result of reading the error it will return the
following:
<html>
 <head>
 <title>Scores Game</title>
 </head>
 <body>
 <body>
 <h1><div id="score" style="color:red">{ERROR}</div></h1>
 </body>
</html>"""

from Score import read_score
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def score_server():
    score = read_score()
    if score:
        message = "<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is : <div id='score'>" + score + "</div></h1> </body></html>"
    else:
        message = "<html> <head> <title>Scores Game</title> </head> <body> <h1><div id='score' style='color:red'>" + score + "</div></h1> </body></html>"
    return message


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
