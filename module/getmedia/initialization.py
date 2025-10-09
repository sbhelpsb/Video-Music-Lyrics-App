"""
獲取媒體初始化
"""
import abc

class Get_Media(abc.ABC):
    """
    獲取媒體
    """
    def __init__(self):
        super().__init__()
    @abc.abstractmethod
    def __str__(self) -> str:
        """
        输出指令形式
        """
        return "Get_Media"
    @abc.abstractmethod
    def __repr__(self) -> str:
        """
        输出调用形式
        """
        return f"Get_Media()"