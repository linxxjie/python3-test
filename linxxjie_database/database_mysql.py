# ==========操作 mysql 数据库==========
import pymysql

# =========创建数据库==========
def create_database():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
    db.close()

# ==========创建表==========
def create_table():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL , name VARCHAR(255) NOT NULL , age INT NOT NULL , PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()

# ==========插入数据==========
def insert_data():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    id = '2013132211'
    user = 'Bob'
    age = 20
    sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()
    db.close()

# ==========插入数据优化==========
def insert_data_optimizing():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    data = {
        'id': '2013132201',
        'name': 'Jack',
        'age': 20
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    # fomat 格式化字符串
    sql = 'INSERT INTO {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Faild')
        db.rollback()
    db.close()

# ==========更新==========
def update_data():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'UPDATE students SET age = %s WHERE name = %s'
    try:
        cursor.execute(sql, (25, 'Bob'))
        db.commit()
    except:
        db.rollback()
    db.close()

# ==========更新优化==========
def update_data_optimizing():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    data = {
        'id': '2013132201',
        'name': 'Bob',
        'age': '21'
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    # ON DUPLICATE KEY UPDATE 如果主键已经存在，就执行更新操作
    sql = 'INSERT INTO {table}({keys}) values ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
    update = ','.join(["{key} = %s".format(key=key) for key in data])
    sql += update
    try:
        if cursor.execute(sql, tuple(data.values()) * 2):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()

# ========== 删除数据 ==========
def delete_data():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    table = 'students'
    condition = 'age > 21'
    sql = 'DELETE FROM {table} where {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

# ==========查询==========
def select_data():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'SELECT * FROM students WHERE age >= 20'
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        # 获取结果的第一条数据
        one = cursor.fetchone()
        print('One', one)
        # 得到所有的结果数据
        results = cursor.fetchall()
        print('Results:', results)
        print('Results Type', type(results))
        for row in results:
            print(row)
    except:
        print('Error')

# ========== 优化查询 ==========
def select_data_optimizing():
    db = pymysql.connect(host='localhost', user='hjhmysql', password='hjhmysql', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'SELECT * FROM students where age >= 20'
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row:', row)
            row = cursor.fetchone()
    except:
        print('Error')
