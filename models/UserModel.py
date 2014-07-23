import BaseModel

class UserModel(BaseModel):
    admin_id = Field()
    admin_name = Field()
    admin_tname = Field()
    admin_type = Field()
    role_id = Field()