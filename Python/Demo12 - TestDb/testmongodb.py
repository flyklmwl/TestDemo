import pymongo 

mongo_url = "172.16.20.33:27017"     	    # 连接到mongodb，如果参数不填，默认为“localhost:27017” 
client = pymongo.MongoClient(mongo_url) 	# 连接到数据库myDatabase 

DATABASE = "webdata" 
db = client[DATABASE]                    #连接到集合(表):myDatabase.myCollection 
COLLECTION = "feiyue" 
db_coll = db[COLLECTION] 

# 搜索全部记录
# all = db_coll.find()
# all = db_coll.find({'tz_title':/游戏/})         # 语法错误！

# 搜索指定记录
# all = db_coll.find({'tz_title':{'$regex':'油猴脚本'}})
# all = db_coll.find({'tz_title':{'$regex':'qq空间'}})
# for record in all:
#     print(record['tz_title'])
#     print(record['tz_link'])
#     print(record['tz_c_time'])

# 复合搜索
# 在表myCollection中寻找date字段等于2017-08-29的记录，并将结果按照age从大到小排序 
# queryArgs = {'date':'2017-08-29'} 

# 保存方法，如果遇到相同的则换_id 继续保存
# if self.db[save_table].update_one(result, {'$setOnInsert': result}, upsert=True):