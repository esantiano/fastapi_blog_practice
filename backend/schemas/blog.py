from typing import Optional
from pydantic import BaseModel, model_validator, ConfigDict
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before") # used to check for title and to create a slug
    def generate_slug(cls, values):
        if 'title' in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values
    
class UpdateBlog(CreateBlog):
    pass

    
class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
