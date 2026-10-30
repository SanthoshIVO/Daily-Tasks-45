'''data validation'''
from pydantic import BaseModel

class TaskSchema(BaseModel):
    # id:str
    title:str
    description:str
    is_completed:bool = False