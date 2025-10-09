import pydantic

class GetListData(pydantic.BaseModel): 
    """
    獲取列表數據結構
    """
    list_name: str
    list_items: list[str]