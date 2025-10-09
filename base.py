import abc


class com_obj(abc.ABC):
    """
    指令模块基类
    """

    def __init__(self):
        """
        初始化
        """

    @abc.abstractmethod
    def __str__(self) -> str:
        """
        输出指令形式
        """
        pass

    @abc.abstractmethod
    def __repr__(self) -> str:
        """
        输出调用形式
        """
        pass
