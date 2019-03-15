import os
import string
from time import strftime

class Disk:
    def __init__(self,path):
        self.path = path

    def get_disk(self):
        """
        :return: 返回当前电脑的磁盘列表
        """
        computer_disk = []
        for c in string.ascii_uppercase:
            c = "%s:"%c
            if os.path.isdir(c):
                computer_disk.append(c)
        return computer_disk

    def get_path_list(self):
        path_lists = []
        path = self.path
        os_list = os.listdir(path)
        print(os_list)
        path_lists = list(map(lambda x:os.path.join(path,"/",x),os_list))
        is_file_list = list(map(lambda x:os.path.isfile(x),path_lists))
        m_time_list = list(map(lambda x:os.path.getmtime(x),path_lists))

        print(path_lists)
        print(is_file_list)
        print(m_time_list)

disk = Disk("C:")
disk.get_path_list()