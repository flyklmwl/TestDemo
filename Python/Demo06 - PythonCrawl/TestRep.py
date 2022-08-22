import re
from pyquery import PyQuery as pq

content = 'This is a Test Program! 点击量: 2232 &nbsp;|&nbsp回复量:3333\n ddd'

content1 = '<a href="thread.php?fid=56">个人日记</a> &gt;&gt;  点击：2155  |  回复数：222  |  ' \
           '发表时间：2018-11-28 19:19  |  <a href="kf_tidfavor.php?action=favor&amp;tid=742454">收藏本帖</a>'

content2 = '<a href="thread.php?fid=56">个人日记</a> &gt;&gt;  点击：-  |  回复数：222  |  ' \
           '发表时间：2018-11-28 19:19  |  <a href="kf_tidfavor.php?action=favor&amp;tid=742454">收藏本帖</a>'

content3 = '''
<tr><td colspan="2" style="line-height:25px;padding-left:5px;"><a href="thread.php?fid=41">Galgame 网络硬盘区</a>&nbsp;&gt;&gt;&nbsp; 点击：- &nbsp;|
&nbsp; 回复数：14 &nbsp;|&nbsp; 发表时间：2018-12-03 23:51 &nbsp;|&nbsp; <a href="kf_tidfavor.php?action=favor&tid=743595">收藏本帖</a></td></tr>
<tr><td width="710" height="50"><div><ul class="pages" style="list-style-type:none;margin:0;padding:0;"><li><a href="read.php?tid=743595&sf=1ab&fpage=0&toread=&page=1">首页</a></li><li><a href="read.php?tid=743595&sf=1ab&fpage=0&toread=&page=0">上一页</a></li><li><a href="javascript:;" style="color:#999999;">- 1 -</a></li><li><a href="read.php?tid=743595&sf=1ab&fpage=0&toread=&page=2">2</a></li><li><a href="read.php?tid=743595&sf=1ab&fpage=0&toread=&page=2">下一页</a></li><li><a href="read.php?tid=743595&sf=1ab&fpage=0&toread=&page=2">…2页</a></li></ul></div></td><td width="250" style="text-align:right;">
<ul class="b_tit2" style="list-style-type:none;margin:0;padding:0;"><li><a href="post.php?action=reply&fid=41&tid=743595" class="b_tit2">回复帖子</a></li><li><a href="javascript:;" class="b_tit2" style="color:#ff7777;" id="read_tui" onclick="read_tui()">推! 2</a></li></ul></td></tr>
'''

# result = re.match('.*点击.*', content)
# print(result)
# print(result.group())
# print(len(content))
# print(result.span())
# print(type(result))
# print(type(content))

# .* 匹配任意字符任意个数
# \d+ 匹配任意数字任意多个
# \s+ 匹配任意非字幕空格
# content2 = '12      3'
# result = re.match('12\s+(\d)', content2)
# print(result.group(1))
# 注意在匹配过程中 '|' 符号要先转义 '\|'


# result = re.match('<a.*</a>.*点击：(\d+|\-)\s+\|\s+回复数：(\d+)', content2)
result = re.search('点击：(\d+|\-).*\|.*回复数：(\d+)', content3, re.S)
# result = re.match('<a.*</a>.*点击：(\d+).*回复数：(\d+)', content1)


print(result.group(1))
print(result.group(2))

