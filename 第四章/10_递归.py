# _*_ encoding: utf-8 _*_
"""
PyCharm 10_递归
2025年07月19日 15时11分14秒
by LiXiaoYang
"""

import os


def test_os():
    # ['1.txt', '2.txt', '3.txt', 'a', 'b']
    print(os.listdir("D:/test"))  # 列出路径下的内容
    # True
    print(os.path.isdir("D:/test/a"))  # 判断指定路径是不是文件夹
    # True
    print(os.path.exists("D:/test"))  # 判断指定路径是否存在


def get_files_recursion_from_dir(path) -> list:
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 文件夹路径
    :return: List：包含所有文件，如果目录不存在或无文件就返回一个空的list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                # 目录是文件夹不是文件
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
        return file_list
    else:
        print("指定目录path不存在")
        return []


if __name__ == '__main__':
    # test_os()
    file_list = get_files_recursion_from_dir("D:/test")
    print(file_list)
