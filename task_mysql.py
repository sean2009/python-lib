import sys

sys.path.append("F:\python\httpsqs\lib")
sys.path.append("F:\python\httpsqs\models")

from models.UserModel import *

user = UserModel(admin_id = 1,admin_name='sdfsf',admin_tname="sfsdf")
user.save()
