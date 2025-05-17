from flask import Blueprint, render_template, request, redirect, url_for
from services import user_login, admin_login, get_all_users, register_new_user, sc_delete_user, sc_modify_user, \
    select_username

user_bp = Blueprint('user', __name__)

'''=====================================================            用户功能实现          ==========================================================='''

'''                                                                   user页面                                                     '''


@user_bp.route('/user')
def user_panel(render_te=None):
    # 渲染普通用户面板模板mplate('user_panel.html')
    return render_template('user/user_panel.html')