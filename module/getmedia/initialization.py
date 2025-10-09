"""
獲取媒體初始化
"""

import abc
from .data import MediaData
import pathlib


class Get_Media(abc.ABC):
    """
    獲取媒體
    """

    def __init__(self, audio_dir: pathlib.Path, lyrics_dir: pathlib.Path):
        """每次加载时执行"""
        super().__init__()

    @abc.abstractmethod
    def initialize(self):
        """第一次加载时执行"""
        pass

    @abc.abstractmethod
    def get_media(self, url: str) -> MediaData:
        """获取媒体"""
        pass
