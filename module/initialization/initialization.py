"""
安裝下載器
"""
from base import com_obj


class Install_Downloader(com_obj):
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