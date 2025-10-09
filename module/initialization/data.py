import pydantic

class initialization(pydantic.BaseModel):
    status: str
    message: str