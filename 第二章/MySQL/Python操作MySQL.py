# _*_ encoding: utf-8 _*_
"""
PyCharm Python操作MySQL
2025年07月17日 19时27分07秒
by LiXiaoYang
"""

from pymysql import Connection

conn = Connection(host='localhost', port=3306, user='root', password='123456', autocommit=True)
# 获取游标对象
cursor = conn.cursor()
conn.select_db('test')
# cursor.execute('create table test_pymysql(id int);')

# print(conn.get_server_info())

# cursor.execute("select * from student")
# result = cursor.fetchall()
# # ((10001, '张三', 20, '男'), (10002, '李四', 21, '男'),
# # (10003, '王五', 19, '女'), (10004, '赵六', 22, '女'), (10005, '钱七', 20, '男'))
# print(result)
# for r in result:
#     print(r)

cursor.execute("insert into student values (10002, '林俊杰', 30, '男')")
# cursor.execute("delete from student where id=1000")
# commit()确认提交
# conn.commit()
conn.close()
