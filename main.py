
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Water Battle , GCP Serverless Hackathon
#adding pyjy

import os
import logging
import random
import jmespath
from flask import Flask, request

#logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
#logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
me = https://python-bot-bl3rxjcqjq-as.a.run.app 

@app.route("/", methods=['POST'])
def move():
    jsondata = request.get_json(force=True)
    #print(jmespath.search('arena.dims[0]', jsondata))
    #print(jmespath.search('arena.dims.state[*]."https://python-bot-fwutkkw3ka-as.a.run.app"[0]', jsondata))
    
    x = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".x', jsondata)
    y = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".y', jsondata)
    direction = jmespath.search('arena.state."https://python-bot-bl3rxjcqjq-as.a.run.app".direction', jsondata)
    print(x)
    print(y)
    print(direction)
    
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
