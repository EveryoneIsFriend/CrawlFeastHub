from werkzeug.security import generate_password_hash, check_password_hash
from database import db_get_user_username, db_get_admin_username, db_list_users, db_register_user, db_delete_user, db_modify_user


'''                                     哈希函数加密                                                       '''
def hash_password(password):
    # 使用werkzeug库的generate_password_hash函数对密码进行哈希处理
    return generate_password_hash(password)

'''                                     哈希函数验证                                                      '''
def verify_password(plain_password, hashed_password):
    # 使用werkzeug库的check_password_hash函数验证密码
    return check_password_hash(hashed_password, plain_password)


'''                                     根据username获取用户信息                                                       '''
def select_username(username):
    return db_get_user_username(username)


'''                                                      用户登录     服务                                                       '''
def user_login(username, password):
    user = db_get_user_username(username)
    print(user)
    if user and verify_password(plain_password=password, hashed_password=user['password']):
        return True
    return False   ##  哈希函数有错误，先打开判断的开关



'''                                                      管理员登录    服务                                                       '''
def admin_login(username, password):   # 管理员登陆服务，调取数据库方法验证，返回bool值
    admin = db_get_admin_username(username)    # 查询获取数据库中username的信息，接受返回的admin的字典信息
    print(admin)
    if admin and verify_password(plain_password=password, hashed_password=admin['password']):
        # 进行用户判空和哈希函数验证密码
        return True
    return False



'''                                                      获取所有用户信息  操作                                                       '''
def get_all_users():
    """查询数据库中的所有用户，并返回用户列表，个人字典"""
    return db_list_users()


'''                                                      注册用户   操作                                                      '''
def register_new_user(username, password, email, phone):
    """注册新用户"""
    hashed_password = hash_password(password) # 使用哈希函数进行一次加密，并返回加密后的密码
    print(username, hashed_password, email, phone)
    return db_register_user(username, hashed_password, email, phone)


'''                                                    管理员修改用户信息//用户修改  操作                                                   '''
def sc_modify_user(username, password, email, phone):
    """修改用户"""
    hashed_password = hash_password(password)
    return db_modify_user(username, hashed_password, email, phone)


'''                                                     管理员删除用户信息//用户注销  操作                                                      '''
def sc_delete_user(username):
    """删除用户"""
    return db_delete_user(username)