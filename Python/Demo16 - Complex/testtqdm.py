from tqdm import trange
from time import sleep
lv = False
num0, num1 = 0, 1
for i in trange(2, desc='loop0', position = num0):
    for j in trange(4, desc='loop1', leave=lv, position=num1):
            #print(j);  #num1 -= 1
            for k in trange(100, desc='loop2', leave=lv, position=2):
                    #num+=1
                    sleep(0.01)