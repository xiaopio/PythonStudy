# _*_ encoding: utf-8 _*_
"""
PyCharm file_util
2025年07月15日 14时59分10秒
by LiXiaoYang
"""


def print_file_info(file_name):
    """
    打印文件中内容到控制台
    :param file_name: 文件路径
    :return: None
    """
    fr = None
    try:
        fr = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"未找到文件{file_name}!,ERROR:{e}")
    else:
        content = fr.read()
        print(content)
    finally:
        if fr:
            fr.close()


def append_to_file(file_name, data):
    """
    文件中追加内容
    :param file_name: 文件路径
    :param data: 追加内容
    :return: None
    """
    with open(file_name, "a", encoding="utf-8") as fr:
        fr.write(data)
        fr.write("\n")


# if __name__ == '__main__':

    # append_to_file("D:/测试.txt", "刘德华,2022-01-04,300000,消费,正式")

    # print_file_info("D:/测试.txt123")
