from pydantic import BaseModel, constr


class TodoCreate(BaseModel):
    content: constr(max_length=250)