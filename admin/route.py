from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for
from services import user_login, admin_login, get_all_users, register_new_user, sc_delete_user, sc_modify_user, select_username

# 创建一个名为 admin 的蓝图
admin_bp = Blueprint('admin', __name__)

"""
1.创建蓝图：在独立的模块中定义蓝图，并指定路由和视图函数。
2.注册蓝图：在主应用中注册蓝图，并设置路由前缀。
3.使用蓝图中的模板和静态文件：将模板和静态文件放在蓝图的 templates 和 static 文件夹中。
4.使用请求钩子和错误处理：在蓝图中定义请求钩子和错误处理函数。
"""

'''=====================================================            管理员  功能实现          ==========================================================='''

'''                                                                  admin页面                                                     '''


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    users = get_all_users()  # 获取所有用户信息
    # 渲染管理员面板模板，并传递用户列表数据
    return render_template('admin/admin.html', users=users)   # 路径要从 templates 根目录开始写


'''                                                   admin修改用户管理   按钮   功能  ===》跳转到 修改用户界面(modify_user.html)                                                '''


@admin_bp.route('/select_user/<string:user_name>', methods=['POST'])
def select_user(user_name):
    print(user_name)
    user = select_username(user_name)
    return render_template('admin/modify_user.html', user=user)


'''                                                                   admin修改用户页面                                                     '''


@admin_bp.route('/modify_user', methods=['POST'])
def modify_user():
    username = request.form['username']  # 获取表单提交的用户名
    password = request.form['password']  # 获取表单提交的密码
    email = request.form['email']  # 获取表单提交的邮箱
    phone = request.form['phone']  # 获取表单提交的电话
    print("修改的用户信息")
    print(username, password, email, phone)
    if sc_modify_user(username, password, email, phone):
        # 如果修改成功，重定向到管理员界面
        return redirect(url_for('admin.admin'))
    # 如果修改失败，返回修改页面并传递错误信息
    return render_template('admin/modify_user.html', error='修改失败')


'''                                                 admin删除用户   按钮   功能   ===》重新访问admin界面  获取                                                 '''


@admin_bp.route('/delete_user/<string:user_name>', methods=['POST'])
def delete_user(user_name):
    print(user_name)
    sc_delete_user(user_name)
    users = get_all_users()  # 获取所有用户信息
    # 渲染管理员面板模板，并传递用户列表数据
    return render_template('admin/admin.html', users=users)



'''                                                 admin添加用户   按钮   功能   ===》调用services.py中的方法，register_new_user  获取                                                 '''


@admin_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']  # 获取表单提交的用户名
        password = request.form['password']  # 获取表单提交的密码
        email = request.form['email']  # 获取表单提交的邮箱
        phone = request.form['phone']  # 获取表单提交的电话
        print("添加用户的信息")
        print(username, password, email, phone)
        if register_new_user(username, password, email, phone):
            # 如果注册成功，重定向到登录页面
            return redirect(url_for('admin.admin'))
        # 如果注册失败，返回注册页面并传递错误信息
        return render_template('admin/add_usre.html', error='Registration failed')
    # 如果是GET请求，返回注册页面
    return render_template('admin/add_user.html')



# 定义蓝图界面的错误请求页面
@admin_bp.errorhandler(404)
def page_not_found(error):
    return 'Page not found', 404
