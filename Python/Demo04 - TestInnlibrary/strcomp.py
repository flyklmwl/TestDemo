import difflib

def stri_similar(s1,s2):
    return difflib.SequenceMatcher(None,s1,s2).quick_ratio()
data1 = '你好啊'
data2 = '你啊'

print(stri_similar(data1, data2))
