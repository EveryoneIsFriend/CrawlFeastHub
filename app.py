from flask import Flask, render_template, request, redirect, url_for
from services import user_login, admin_login, get_all_users, register_new_user, sc_delete_user, sc_modify_user, \
    select_username

'''    在 Flask 中
render_template 主要用于生成并返回动态的 HTML 页面 (渲染加载前端页面)
redirect 用于引导客户端去请求另一个 URL (重定向)
url_for() 最常见的用法是通过视图函数的名称来生成对应的 URL (动态生成一个新的url，根据@app.route('/')的路由)
request对象是一个非常重要的工具，用于处理客户端发送到服务器的 HTTP 请求
'''

app = Flask(__name__)

# 导入蓝图
from auth.route import auth_bp
from admin.route import admin_bp
from menu.route import menu_bp
from user.route import user_bp

# 创建蓝图
app.register_blueprint(
    auth_bp,
    url_prefix='/auth',  # 注册 auth 蓝图，并将所有的路由前缀设置为 /auth。
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

app.register_blueprint(
    admin_bp,
    url_prefix='/admin',
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

app.register_blueprint(
    menu_bp,
    url_prefix='/menu',
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

app.register_blueprint(
    user_bp,
    url_prefix='/user',
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

app.secret_key = 'your_secret_key'  # 设置Flask应用的密钥，用于加密会话等 Sessions

'''                                             起始页，重定向到登录页面                                '''


@app.route('/')
def index():
    # 根路由重定向到登录页面
    return redirect(url_for('auth.login'))
    # 在 Flask 框架中，url_for() 是一个非常有用的函数，主要用于生成 URL
    # url_for() 最常见的用法是通过视图函数的名称来生成对应的 URL


'''=====================================================         爬虫、可视化、网络接口   功能实现          ==========================================================='''

'''=====================================================                    主程序入口               ==========================================================='''
if __name__ == '__main__':
    print('starting app...')
    print('app running on http://127.0.0.1:5000/')
    app.run(debug=True)  # 启动Flask应用，开启调试模式,热部署
