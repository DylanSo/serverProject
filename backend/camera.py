import cv2
import os

import gol
from detect import main, parse_opt
import argparse

UPLOAD_FOLDER = 'data/images/'


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        os.remove(c_path)


def cam():
    # del_file(UPLOAD_FOLDER)  # 删除原来的图片 先不删
    source = cv2.VideoCapture('text.mp4')  # 源
    cnt = 1
    time = 10  # 抽取帧间隔时间
    while True:  # 存一张检测一张 有错误时break
        ret, frame = source.read()
        if not ret:
            break
        if cnt % time == 0:
            name = str(int(cnt / time)) + '.jpg'
            cv2.imwrite(UPLOAD_FOLDER + name, frame)  # 存储
            # os.system('python detect.py --source ' + UPLOAD_FOLDER + name)
            # ↑这样的话gol会崩
            opt = parse_opt(name)  # 检测
            main(opt)
        cnt += 1

        if gol.get_value('cnt') > 0:  # 有错误时break 在detect里面改的
            return name  # 返回图片名
            break

    source.release()
