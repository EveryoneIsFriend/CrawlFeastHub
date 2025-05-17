from flask import Blueprint, render_template, request, redirect, url_for
from services import user_login, admin_login, get_all_users, register_new_user, sc_delete_user, sc_modify_user, \
    select_username

auth_bp = Blueprint('auth', __name__)

'''                                            登录页面                                                     '''


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']  # 获取表单提交的用户名
        password = request.form['password']  # 获取表单提交的密码
        user_type = request.form.get('user_type', 'user')  # 获取用户选择的用户类型，默认为普通用户
        print("登录信息")
        print(f'用户名:{username}, 密码:{password}, 用户类型:{user_type}')

        if user_type == 'admin':
            if admin_login(username, password):
                # 如果是管理员登录且验证成功，重定向到管理员面板
                return redirect(url_for('admin.admin'))
        else:
            if user_login(username, password):
                # 如果是普通用户登录且验证成功，重定向到普通用户面板  user_panel函数
                return redirect(url_for('user.user_panel'))
        # 如果登录失败，返回登录页面并传递错误信息
        return render_template('auth/login.html', error='用户名或密码错误！')
    # 如果是GET请求，返回登录页面
    return render_template('auth/login.html')


'''                                              注册页面                                                     '''


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']  # 获取表单提交的用户名
        password = request.form['password']  # 获取表单提交的密码
        email = request.form['email']  # 获取表单提交的邮箱
        phone = request.form['phone']  # 获取表单提交的电话
        print("注册提交的信息")
        print(username, password, email, phone)
        if register_new_user(username, password, email, phone):
            # 如果注册成功，重定向到登录页面
            return redirect(url_for('auth.login'))
        # 如果注册失败，返回注册页面并传递错误信息
        return render_template('auth/register.html', error='Registration failed')
    # 如果是GET请求，返回注册页面
    return render_template('auth/register.html')
