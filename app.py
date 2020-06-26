from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask (__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
     return render_template("index.html")

@app.route('/api/list', methods=['GET'])
def matzip_list():
     matzips = list(db.matzip.find({},{'_id':False}))
	return jsonify({'result': 'success','matzip_list': matzips})

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)