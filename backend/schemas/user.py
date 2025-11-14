from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=4)

class ShowUser(BaseModel): # used for return information from the api, mainly to hide the password
    id: int
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
