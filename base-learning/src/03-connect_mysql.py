# coding=utf-8
# 测试连接数据库mysql
import MySQLdb

'''
        :param str host:        host to connect
        :param str user:        user to connect as
        :param str password:    password to use
        :param str passwd:      alias of password, for backward compatibility
        :param str database:    database to use
        :param str db:          alias of database, for backward compatibility
        :param int port:        TCP/IP port to connect to
'''

try:
    # 获得连接
    conn = MySQLdb.connect(host="hadoop1", user="ooooo", password="123456", db="pythonlearning", charset="utf8")

    # 获得游标对象cursor
    cursor = conn.cursor()

    # 插入数据
    rowCount = cursor.execute("INSERT  into tb_student (id, name, age, sex) VALUES (NULL ,'zhangsan',18,1)")
    print('插入数据影响的行数：%d' % rowCount)
    conn.commit()

    # 查询数据,并获取数据
    rowCount = cursor.execute('select * from tb_student')
    print("查询数据的总记录数：%d" % rowCount)
    results = cursor.fetchall()
    for result in results:
        print(result)

    rowCount = cursor.execute("delete from tb_student WHERE  id = 1")
    conn.commit()
    print("删除数据影响的行数: %d" % rowCount)
    rowCount = cursor.execute('select * from tb_student')
    print("查询数据的总记录数：%d" % rowCount)

    rowCount = cursor.execute('update tb_student set name = "lisi" WHERE  id  = 5')
    conn.commit()

    print("更新数据的影响的行数：%d" % rowCount)

    # 关闭资源
    cursor.close()
    conn.close()

    for i in results:
        print(i)

except Exception as e:
    pass
