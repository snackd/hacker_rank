import os

# folder_path = os.path.abspath(os.getcwd())
# file_name = os.path.basename(__file__)[:-3] + '.txt'
# abs_path = folder_path + "\\" + file_name


class SelfPath:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.folder_path = os.path.abspath(os.getcwd())
        self.file_name = os.path.basename(__file__)[:-3] + '.txt'
        self.abs_path = self.folder_path + "\\" + self.file_name

    def get_file_path(self, n):
        self.file_name = os.path.basename(n)[:-3] + '.txt'
        print(self.file_name)
