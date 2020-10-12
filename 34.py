#! /usr/bin/python
# -*- coding: utf-8 -*-
# 图片上传七牛云

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from qiniu import BucketManager
import sys, time
import os
import msvcrt
import subprocess
from datetime import datetime

# you will get md_url in this file
result_file = "./qiniu/ss.txt"

if os.path.exists(result_file):
    os.remove(result_file)
os.chdir(sys.path[0])

access_key = 'jCvcWK1m4OgH1ZIrvcwuOhUUlY-I09B0KNk8YbfT'
secret_key = 'AUfJZZBQAZIERUbvq6Zt-gI9TUGzzrhFp9MiuTRM'
bucket_name = 'cartoon123'
bucket_url = 'qhx8yqe57.hn-bkt.clouddn.com'
md_url_result = "md_url.txt"  # 链接保存的位置

img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]


def upload_img(bucket_name, file_name, file_path):
    # generate token
    token = q.upload_token(bucket_name, file_name, 3600)
    info = put_file(token, file_name, file_path)
    # delete local imgFile
    # os.remove(file_path)
    return


def get_img_url(bucket_url, file_name):
    # date=datetime.now().strftime('%Y%m%d_%H%M%S')
    # file_names = file_name+'?'+date
    img_url = 'http://%s/%s' % (bucket_url, file_name)
    # generate md_url
    md_url = "![%s](%s)\n" % (file_name, img_url)
    return md_url


def save_to_txt(bucket_url, file_name):
    url_before_save = get_img_url(bucket_url, file_name)
    # save to clipBoard
    addToClipBoard(url_before_save)
    # save md_url to txt
    with open(md_url_result, "a") as f:
        f.write(url_before_save)
    return


# save to clipboard
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


# get filename of .md in current index
def getMarkName(paths):
    f_list = os.listdir(paths)
    for i in f_list:
        name = os.path.splitext(i)[0]
        end = os.path.splitext(i)[1]
        if end == '.md':
            return name + '_'
    return 'markdown'


if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    imgs = sys.argv[1:]

    for img in imgs:
        # name for img with local time
        up_filename = getMarkName(os.getcwd().replace(
            '\\', '/')) + os.path.split(img)[1]
        upload_img(bucket_name, up_filename, img)
        save_to_txt(bucket_url, up_filename)
