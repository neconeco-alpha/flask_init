from collections import defaultdict
from flask_login import UserMixin

class User(UserMixin):
  def __init__(self, id, name, pswd):
    self.id = id
    self.name = name
    self.pswd = pswd

users = {
  1: User(1, "user01", "pass"),
  2: User(2, "user02", "pass")
}

nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
  user_check[i.name]["pswd"] = i.pswd
  user_check[i.name]["id"] = i.id
