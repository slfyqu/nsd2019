import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1902',
    charset='utf8'
)

# 创建游标，用于将来执行SQL语句
cursor = conn.cursor()
#################################
# 向部门表中插入数据
# 编写SQL语句
insert_dep = 'INSERT INTO departments VALUES (%s, %s)'
# 填写每个部门的字段值
hr = (1, '人事部')
ops = (2, '运维部')
dev = (3, '开发部')
qa = (4, '测试部')
market = (5, '市场部')
deps = [ops, dev, qa]
# 执行sql语句
cursor.execute(insert_dep, hr)   # 插入一条数据
cursor.executemany(insert_dep, deps)  # 插入多条数据
cursor.executemany(insert_dep, [market])
##################################
# 确认
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()