import os
import gol
import cv2
from camera import cam
from detect import main, parse_opt
from flask import Flask, render_template, request, Response, jsonify

UPLOAD_FOLDER = 'data/images'
RESULT_FOLDER = 'static/detect/exp'

gol._init()
gol.set_value('name', 0)
gol.set_value('cnt', 0)
app = Flask(__name__)


@app.route('/api')  # 开始界面
def index():
    return render_template('index.html')


@app.route('/api/webcam')  # 按下开始键
def webcam():
    # if 按开始键
    return render_template('success.html', img=cam(), ord=gol.get_value('name'))  # vue的话这个地方要改


@app.route('/api/post', methods=['POST'])  # 收到了文件或者文件夹
def post():
    if request.method == 'POST':
        f = request.files['file1']  # 把文件内容取出来 文件夹就加个循环？
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))  # 保存
        opt = parse_opt(f.filename)
        main(opt)
        return render_template('success.html', name=f.filename, ord=gol.get_value('name'))  # 文件名传给succsess


if __name__ == '__main__':
    app.run(debug=False)
