# 让电脑可以支持服务访问
# 需要一个web框架
# conda install Flask
# pip install Flask
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

hero = ["通通", "耕耘", "华仔", "老王", "鸿宝", "123"]

# 访问的地址参数
@app.route("/index")
def index():
    return render_template('index.html', hero=hero)


@app.route('/choujiang')
def choujiang():
    num = randint(0, len(hero))
    return render_template('index.html', hero=hero, h=hero[num])


# 运行  debug=True ==> 热执行
app.run(debug=True)
