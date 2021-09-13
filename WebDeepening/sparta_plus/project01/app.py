from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_plus_week1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    diaries = list(db.diary.find({}, {'_id': False}))
    return jsonify({'all_diary': diaries})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    doc = {
        'title': title_receive,
        'content': content_receive
    }

    db.diary.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)