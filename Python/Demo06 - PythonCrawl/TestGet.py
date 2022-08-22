from pyquery import PyQuery as pq

str = '''
<table width="860" cellspacing="0" cellpadding="0" align="center">&#13;
<tr><td colspan="2" style="border-bottom:1px solid #CCCCFF;">&#13;
<span style="font-size:18px;line-height:35px;font-weight:bold;">0.2贡献抽光环到70的留言楼层前随机选五楼（0.2贡献×5），长期记录贴</span></td></tr>&#13;
<tr><td colspan="2" style="line-height:25px;padding-left:5px;"><a href="thread.php?fid=56">个人日记</a> &gt;&gt;  点击：2155  |  回复数：222  |  发表时间：2018-11-28 19:19  |  <a href="kf_tidfavor.php?action=favor&amp;tid=742454">收藏本帖</a></td></tr>&#13;
<tr><td width="710" height="50"><div><ul class="pages" style="list-style-type:none;margin:0;padding:0;"><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=1">首页</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=0">上一页</a></li><li><a href="javascript:;" style="color:#999999;">- 1 -</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=2">2</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=3">3</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=4">4</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=5">5</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=2">下一页</a></li><li><a href="read.php?tid=742454&amp;sf=b09&amp;fpage=0&amp;toread=&amp;page=23">…23页</a></li></ul></div></td><td width="250" style="text-align:right;">&#13;
<ul class="b_tit2" style="list-style-type:none;margin:0;padding:0;"><li><a href="post.php?action=reply&amp;fid=56&amp;tid=742454" class="b_tit2">回复帖子</a></li><li><a href="javascript:;" class="b_tit2" style="color:#ff7777;" id="read_tui" onclick="read_tui()">推! 2</a></li></ul></td></tr>&#13;
&#13;
</table>
'''
index = pq(str)
print(index('tr:nth-child(2) a'))

