"""
獲取列表初始化
"""
import abc
from .data import GetListData


class Get_List(abc.ABC):
    """
    獲取列表
    """
    def __init__(self, list_name: str):
        super().__init__()

    @abc.abstractmethod
    def get_list(self) -> GetListData:
        """
        獲取列表
        """
        pass