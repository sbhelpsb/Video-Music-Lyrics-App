"""
獲取列表初始化
"""
import abc

class Get_List(abc.ABC):
    """
    獲取列表
    """
    def __init__(self):
        super().__init__()
    @abc.abstractmethod
    def __str__(self) -> str:
        """
        输出指令形式
        """
        return "Get_List"
    @abc.abstractmethod
    def __repr__(self) -> str:
        """
        输出调用形式
        """
        return f"Get_List()"