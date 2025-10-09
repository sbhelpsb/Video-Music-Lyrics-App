"""
安裝下載器
"""
import abc


class Install_Downloader(abc.ABC):
    """
    安裝下載器
    """
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        """
        输出指令形式
        """
        return "Install_Downloader"

    def __repr__(self) -> str:
        """
        输出调用形式
        """
        return f"Install_Downloader()"