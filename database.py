import pymysql
from config import DB_CONFIG


'''                                            建立数据库链接函数                                                     '''
def get_connection():
    # 使用配置信息建立数据库连接
    return pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        port=DB_CONFIG['port']
    )

'''                                            获取用户信息（根据username）  ===》  单个用户信息  or   None                                                  '''
def db_get_user_username(username):
    # 根据用户名查询用户信息  返回用户信息字典 or None
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 根据用户名查询用户信息的SQL语句
            # sql = f'SELECT * FROM users WHERE username = {username}'   安全性较差，容易被SQL注入攻击  所以使用游标函数进行SQL语句的执行
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))

            # 执行了一个查询语句，数据库返回了一个结果集(元祖),查询不到返回None值
            result = cursor.fetchone()
            if result:
                # 将查询结果整理为字典形式返回
                user = {
                    'id': result[0],
                    'username': result[1],
                    'password': result[2],
                    'email': result[3],
                    'phone': result[4],
                    'registered_at': result[5]
                }
                return user
            return None
    finally:
        conn.close()


'''                                            获取管理员信息（根据username）  ===》  单个管理员信息  or   None                                                   '''
def db_get_admin_username(username):
    # 根据用户名查询管理员信息 返回管理员信息字典 or None
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 根据用户名查询管理员信息的SQL语句
            sql = "SELECT * FROM admins WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                # 将查询结果整理为字典形式返回
                admin = {
                    'id': result[0],
                    'username': result[1],
                    'password': result[2],
                    'email': result[3],
                    'created_at': result[4]
                }
                return admin
            return None
    finally:
        conn.close()


'''                                            获取所有的用户信息  ===》  用户列表                                                '''
def db_list_users():
    #  查询数据库中的所有用户   并返回用户列表
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 查询所有用户信息的SQL语句
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for row in results:
                # 将每一行查询结果整理为字典形式，添加到用户列表中
                user = {
                    'id': row[0],
                    'username': row[1],
                    'password': row[2],
                    'email': row[3],
                    'phone': row[4],
                    'registered_at': row[5]
                }
                users.append(user)
            return users
    finally:
        conn.close()


'''                                             注册用户  users   ===》  True  or   Flase                                               '''
def db_register_user(username, password, email, phone):
    #   管理员权限  ----------》  注册用户
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 插入新用户信息的SQL语句
            sql = "INSERT INTO users (username, password, email, phone) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (username, password, email, phone))
            conn.commit()
            return True
    except pymysql.Error as e:
        conn.rollback()
        # 关键改进：记录数据库操作中出现的错误信息，方便找出问题
        print(f"数据库错误: {e}")
        print(f"错误代码: {e.args[0]}")
        print(f"错误信息: {e.args[1]}")
        return False
    finally:
        conn.close()

'''                                                   修改用户  users   ===》  True  or   Flase                                               '''
def db_modify_user(username, password, email, phone):
    #   管理员权限  ----------》  修改用户
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 修改用户信息的SQL语句
            sql = "UPDATE users SET password = %s, email = %s, phone = %s WHERE username = %s"
            cursor.execute(sql, (password, email, phone, username))
            conn.commit()
            return True
    except pymysql.Error as e:
        conn.rollback()
        # 关键改进：记录数据库操作中出现的错误信息，方便找出问题
        print(f"数据库错误: {e}")
        print(f"错误代码: {e.args[0]}")
        print(f"错误信息: {e.args[1]}")
        return False
    finally:
        conn.close()


'''                                                   删除用户 users    ===》   True  or   Flase                                                  '''
def db_delete_user(username):
    #   管理员权限  ----------》  删除用户
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 删除用户信息的SQL语句
            sql = "DELETE FROM users WHERE username = %s"
            cursor.execute(sql, username)
            conn.commit()
            return True
    except pymysql.Error as e:
        conn.rollback()
        # 关键改进：记录数据库操作中出现的错误信息，方便找出问题
        print(f"数据库错误: {e}")
        print(f"错误代码: {e.args[0]}")
        print(f"错误信息: {e.args[1]}")
        return False
    finally:
        conn.close()