
# Water Battle , GCP Serverless Hackathon

import os
import logging
import random
import jmespath
from flask import Flask, request

#logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
#logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['POST'])
def move():
    jsondata = request.get_json(force=True)
    x = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".x', jsondata)
    y = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".y', jsondata)
    direction = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".direction', jsondata)
    print(x)
    print(y)
    print(direction)
    x1 = x - 1
    x2 = x + 1
    y1 = y - 1
    y2 = y + 1
    print(x1)
    print(x2)
    print(y1)
    print(y2)

    bool1 = contains(jmespath.search('arena.state.*.x', jsondata), x1)
    print(bool1)
    return moves[random.randrange(len(moves))]
     
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
