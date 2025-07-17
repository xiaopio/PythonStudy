# _*_ encoding: utf-8 _*_
"""
PyCharm file_define
2025年07月17日 15时56分02秒
by LiXiaoYang
"""
import json

from data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        _f = open(self.path, 'r', encoding='utf-8')
        for line in _f.readlines():
            # 消除读取到每一行的换行符
            line = line.strip()
            data = line.split(',')
            record_list.append(Record(data[0], data[1], int(data[2]), data[3]))
        _f.close()
        return record_list


class JSONFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        _f = open(self.path, 'r', encoding='utf-8')
        for line in _f.readlines():
            line = line.strip()
            data = json.loads(line)
            record_list.append(Record(data['date'], data['order_id'], int(data['money']), data['province']))
        _f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader('2011年1月销售数据.txt')
    datas_1 = text_file_reader.read_data()
    for data in datas_1:
        print(data)
    json_file_reader = JSONFileReader('2011年2月销售数据JSON.txt')
    datas_2 = json_file_reader.read_data()

    for data in datas_2:
        print(data)
