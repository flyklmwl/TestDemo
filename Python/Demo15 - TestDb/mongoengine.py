from mongoengine import *
disconnect()
connect('webdata', host='172.16.20.33', port=27017)
import datetime
class feiyue(Document):

    # name = StringField(required=True, max_length=200)
    # age = IntField(required=True)

tz_title = StringField(required=True)
tz_type = StringField(required=True)
tz_dj = StringField(required=True)
tz_tui = StringField(required=True)
tz_hf = StringField(required=True)
tz_c_time = StringField(required=True)
tz_link = StringField(required=True)
tz_lz = StringField(required=True)

users = feiyue.objects.all() #返回所有的文档对象列表
djs = feiyue.objects(tz_dj__gte=5000)
for u in djs:
print("name:",u.tz_title,",dj:",u.tz_dj)

# print(users.count())
# for u in users:
#    print("name:",u.tz_title,",age:",u.tz_type)