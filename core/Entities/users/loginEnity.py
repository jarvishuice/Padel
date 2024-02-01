from pydantic import BaseModel
class LoginEntity(BaseModel):
    userName:str
    password:str

