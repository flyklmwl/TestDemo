from pyquery import PyQuery as pq

html = '''
<div id='container'>
    <ul class=list>
        <li class='item-0'>firest item</li>
        <li class='item-1'><a href='link2.html'>second item</a></li>
        <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
        <li class='item-0'><a href='link5.html'>fifth item</a></li>
    </ul>
</div>
'''
# 字符串初始化、url初始化、文件初始化
doc = pq(html)                  # 这里是把html 转换成PyQuery对象
# print(html)
# print(doc)

# 利用css选择器定位PyQuery对象
# print(doc('li'))                # PyQuery 对象就可以直接css选择器
# print(doc('#container'))           # #表示选择id    .表示类
# print(doc('#container .item-1 a'))  # 这种不一定需要父子关系，只要是层级就会选到

# 利用find查找 定位PyQuery对象
print(type(doc))                 # 可以查看doc的类型
items = doc('.list')
print(type(items))
print(items.find('.item-1 a'))   # find 也可以支持级联查找
print(type(items.find('a')))     # 使用find找到的类型也是PyQuery类型

