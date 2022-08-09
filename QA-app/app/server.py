from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__, template_folder="template")


@app.route('/')
def home():
    endpoint = 'https://lambda-s3-file.s3.ap-northeast-1.amazonaws.com/qa-app/'
    file_num = random.randint(1,40)
    fpath = endpoint + str(file_num) + '.pdf'
    return render_template('top.html', fpath=fpath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
