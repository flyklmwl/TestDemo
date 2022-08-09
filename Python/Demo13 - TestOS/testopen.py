txt_line = 0

with open('e:/filename.txt', encoding='utf-8') as f:
  for line in f.readlines():##readlines(),函数把所有的行都读取进来；
    txt = line.strip()##删除行后的换行符，img_file 就是每行的内容啦
    txt_line += 1
    print(f"总行数为: {txt_line}")
    # print(txt)
