from flask import Flask,jsonify, request
import requests


app=Flask(__name__)
app.config.from_object(__name__)

Debug = False

@app.route('/ping', methods=['GET'])
def ping():
    '''This function returns pong!'''
    return jsonify('pong!')

@app.route('/word', methods=['GET'])
def random_word():
    '''this functon pulls a random word from the api and reverse the word and upper case it '''
    word = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    split_word = word.json()[0][::-1]
    return jsonify(split_word.upper())

@app.route('/string-count', methods=['POST'])
def string_count():
    '''this pulls a random word from the api and gets the length of the string'''
    string = request.get('https://random-word-api.herokuapp.com/word?number=1').json()[0]
    return jsonify(len(string))

if __name__ == '__main__':
    app.run()

# Modification of https://flask.palletsprojects.com/en/2.1.x/errorhandling/#generic-exception-handlers
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
