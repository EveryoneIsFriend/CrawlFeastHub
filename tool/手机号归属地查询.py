
from flask import Flask, request, render_template  # web框架
import requests          # 发送请求模块
from lxml import etree   # 解析数据模块


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}

# 创建一个可以支持web应用的框架
app = Flask(__name__)


def get_moblie(phone):
    # 发送请求的地址
    url = f"https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile"
    # 发送请求
    resp = requests.get(url, headers=headers)

    # 设置中文显示
    resp.encoding = 'utf-8'

    # 解析数据
    e = etree.HTML(resp.text)
    # 编写Xpath提取数据      //：其中 // 表示任意后代层级
    datas = e.xpath('//tr/td[2]/span//text() | //tr/td[2]//a//text()')

    # 解析响应
    print(datas)
    return datas


@app.route('/')
def index():
    return render_template('search_phone.html', data="")

@app.route('/search_phone')  # 建立路由
def search_phone():

    phone_tell = request.args.get('phone')
    print(phone_tell)
    if not phone_tell.isdigit() or len(phone_tell) != 11:
        return "请输入有效的11位手机号码！"
    datas = get_moblie(phone_tell)
    print(datas)
    return render_template('search_phone.html', data=datas)
    # return get_moblie(phone_tell)



app.run(debug=True)
