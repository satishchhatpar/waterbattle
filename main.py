
# Water Battle , GCP Serverless Hackathon
#anthos

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
    return 'T'


if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
