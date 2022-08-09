from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__, template_folder="template")


@app.route('/')
def q():
    endpoint = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app-v2/'
    file_num = random.randrange(1, 80, 2)
    fpath = endpoint + str(file_num) + '.pdf'
    return render_template('top.html', fpath=fpath, id=file_num)


@app.route('/a/<int:id>')
def a(id):
    endpoint = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app-v2/'
    file_num = random.randint(1,40)
    fpath = endpoint + str(id+1) + '.pdf'
    return render_template('answer.html', fpath=fpath)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
