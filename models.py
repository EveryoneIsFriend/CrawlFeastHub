class User:
    def __init__(self, id=None, username=None, password=None, email=None, phone=None, registered_at=None):
        self.id = id  # 用户ID，唯一标识用户
        self.username = username  # 用户名
        self.password = password  # 用户密码，哈希值存储
        self.email = email  # 邮箱
        self.phone = phone  # 电话
        self.registered_at = registered_at  # 用户注册时间

class Admin:
    def __init__(self, id=None, username=None, password=None, email=None, created_at=None):
        self.id = id  # 管理员ID，唯一标识管理员
        self.username = username  # 管理员用户名
        self.password = password  # 管理员密码，哈希值存储
        self.email = email  # 管理员邮箱
        self.created_at = created_at  # 管理员创建时间


class Menu:
    def __init__(self, id=None, menu_code=None, menu_name=None, menu_wen=None) -> None:
        
        pass