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
    fpath = endpoint + str(id+1) + '.pdf'
    return render_template('answer.html', fpath=fpath)

@app.route('/order')
def order():
    fpath = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app-v2/1.pdf'
    return render_template('order.html', fpath=fpath, file_num=1)

@app.route('/order/a/<int:id>')
def order_a(id):
    endpoint = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app-v2/'
    file_num = id +1
    fpath = endpoint + str(file_num) + '.pdf'
    return render_template('order_a.html', fpath=fpath, file_num=file_num)

@app.route('/order/q/<int:id>')
def order_q(id):
    endpoint = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app-v2/'
    file_num = id +1
    fpath = endpoint + str(file_num) + '.pdf'
    return render_template('order_q.html', fpath=fpath, file_num=file_num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
