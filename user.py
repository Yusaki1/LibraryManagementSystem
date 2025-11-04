class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def register(self):
        print(f"用户注册：{self.name}（ID：{self.user_id}）")
