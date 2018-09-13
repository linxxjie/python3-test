import pymongo
from bson.objectid import ObjectId
# ========== MongoDB基本操作 ==========
# 插入数据
def database_insert(collection):
    student = {
        'id': '2013132211',
        'name': 'linxxjie',
        'age': 24,
        'gender': 'female'
    }
    student1 = {
        'id': '2013132201',
        'name': 'Mike',
        'age': 24,
        'gender': 'male'
    }
    student2 = {
        'id': '2013132202',
        'name': 'Jordan',
        'age': 24,
        'gender': 'male'
    }
    # pyMongo 3.x 版本中，官方已经不推荐使用insert（）
    result_one = collection.insert(student)
    result = collection.insert([student1, student2])
    print(result_one)
    print(result)

def database_insert_one(collection):
    student3 = {
        'id': '2013132203',
        'name': 'Jack',
        'age': 24,
        'gender': 'male'
    }
    result = collection.insert_one(student3)
    print(result)

def database_insert_many(collection):
    student4 = {
        'id': '2013132204',
        'name': 'Jack',
        'age': 24,
        'gender': 'male'
    }
    student5 = {
        'id': '2013132205',
        'name': 'Jack',
        'age': 24,
        'gender': 'male'
    }
    result = collection.insert_many([student4, student5])
    print(result)
    print(result.inserted_ids)

# 查询
def database_select_find_one(collection):
    result = collection.find_one({'name': 'linxxjie'})
    print(type(result))
    print(result)

# 根据objectId查询
def database_select_by_objectId(collection):
    result = collection.find_one({'_id': ObjectId('5b9a0ad9977c693e54fefd0b')})
    print(result)

# 查询多条
def database_select_find(collection):
    # results = collection.find({'age': 24})
    # 大于20
    # results = collection.find({'age': {'$gt': 20}})
    # 正则
    # results = collection.find({'name': {'$regex': '^M.*'}})
    results = collection.find()
    print(results)
    for result in results:
        print(result)

# 计数
def database_count(collection):
    count = collection.find().count()
    print(count)

# 排序
def database_sort(collection):
    # 升序
    results = collection.find().sort('name', pymongo.ASCENDING)
    print([result['name'] for result in results])

# 偏移
def database_skip(collection):
    results = collection.find().sort('name', pymongo.ASCENDING).skip(5).limit(2)
    print([result['name'] for result in results])

# 更新
def database_update(collection):
    condition = {'name': 'Jack'}
    student = collection.find_one(condition)
    print(student)
    student['age'] = 24
    # 官方不推荐update
    # result = collection.update(condition, student)
    # result = collection.update(condition, {'$set': student})
    # update_one
    result = collection.update_one(condition, {'$set': student})
    print(result)
    # 数据条数、受影响的数据条数
    print(result.matched_count, result.modified_count)

def database_update_many(collection):
    ccondition = {'age': {'$gt': 20}}
    result = collection.update_many(ccondition, {'$inc': {'age': 1}})
    print(result)
    print(result.matched_count, result.modified_count)

# 删除
def database_remove(collection):
    result = collection.remove({'name': 'Jack'})
    print(result)

def database_delete(collection):
    result = collection.delete_one({'name': 'Tome'})
    print(result)
    print(result.deleted_count)
    result = collection.delete_many({'age': {'$lt': 25}})
    print(result.deleted_count)

if __name__ == '__main__':
    # 连接 MongoDB
    # client = pymongo.MongoClient(host='localhost', post=27017)
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # 指定数据库
    db = client.test
    # db = client['test']
    # 指定集合
    collection = db.students
    # collection = db['students']
    database_select_find(collection)
    # database_delete(collection)

