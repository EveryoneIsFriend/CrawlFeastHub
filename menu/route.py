from flask import Blueprint, render_template, request, redirect, url_for
from services import user_login, admin_login, get_all_users, register_new_user, sc_delete_user, sc_modify_user, \
    select_username

menu_bp = Blueprint('menu', __name__)

'''=====================================================        菜单主页展示  功能实现          ==========================================================='''


@menu_bp.route('/menu_main')
def menu_main():
    return render_template('menu/menu_main.html')