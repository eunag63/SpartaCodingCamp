from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def main():
    myname = "코기"
    return render_template("index.html", name=myname)


@app.route('/detail/<keyword>')
def detail(keyword):
    # word API
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization": "Token 7e530070d87fefd64570d05ee1e2db30d67332b4"})
    result = r.json()
    print(result)

    # 받아오기
    word_receive = request.args.get("word_give")
    print(word_receive)

    return render_template("detail.html", word=keyword)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)