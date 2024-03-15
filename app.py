import os
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def random_number():
    string = ''
    for i in range (0,100):
        string += str(random.randrange(i,100)) + '\n'
    return string
        
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)