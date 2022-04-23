from typing import Optional
import TextFile, BinaryFile


class Folder:
    def __init__(self, file_list: list[Optional[TextFile, BinaryFile]]):
        self.files = file_list
