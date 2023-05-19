from pydantic import BaseModel


class UserBasemodel(BaseModel):
    username:str
    password:str