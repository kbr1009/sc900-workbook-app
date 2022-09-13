from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__, template_folder="template")
s3_endpoint = "https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/"

@app.route('/')
def top():
    return render_template('top.html')


"""
ランダムに出題
"""
@app.route('/<string:category>')
def q(category):
    # category ->  sc900  az900  (s3のフォルダ名)
    rand_num = None
    if category == "az900":
        rand_num = 100
    if category == "sc900":
        rand_num = 80

    master_pdf = s3_endpoint + category + '/' + category + ".pdf"
    file_num = random.randrange(1, rand_num , 2)
    fpath = s3_endpoint + category + '/' + str(file_num) + '.pdf'
    return render_template('rand_q.html', fpath=fpath, id=file_num, category=category, master_pdf=master_pdf)


"""
ランダムに出題->解答
"""
@app.route('/<string:category>/<int:id>')
def a(category, id):
    fpath = s3_endpoint + category + '/' + str(id+1) + '.pdf'
    master_pdf = s3_endpoint + category + '/' + category + ".pdf"
    return render_template('rand_a.html', fpath=fpath, category=category, master_pdf=master_pdf)


"""
順番に出題
"""
@app.route('/<string:category>/order')
def order(category):
    fpath = s3_endpoint + category + '/1.pdf'
    return render_template('order.html', fpath=fpath, file_num=1, category=category)


"""
順番に出題->解答
"""
@app.route('/<string:category>/order/<int:id>')
def order_a(category, id):
    fpath = s3_endpoint + category + '/' + str(id+1) + '.pdf'
    return render_template('order_a.html', fpath=fpath, file_num=id+1, category=category)


"""
順番に出題->解答->質問
"""
@app.route('/<string:category>/order/q/<int:id>')
def order_q(category, id):
    fpath = s3_endpoint + category + '/' + str(id+1) + '.pdf'
    return render_template('order_q.html', fpath=fpath, file_num=id+1, category=category)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
