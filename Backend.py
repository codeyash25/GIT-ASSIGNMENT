from flask import Flask , request , render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('database_url')
client = MongoClient(MONGO_URI , server_api=ServerApi('1'))
db = client.test
collection = db['GIT-ASSIGNMENT Q&A']

app = Flask(__name__)

@app.route('/')
def Home():
  return render_template('index.html')

@app.route('/submit' , methods=['POST'])
def submit():
  Iname= request.form.get('ItemName')
  Idesc = request.form.get('ItemDescription')
  collection.insert_one({
    'Item Name' : Iname,
    'Item Description' : Idesc
  })
  print()
  return "submit data"
if __name__ == '__main__':
    app.run(debug=True)