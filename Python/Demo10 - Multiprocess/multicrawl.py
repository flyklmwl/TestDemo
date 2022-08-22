# 多线程爬取

import requests
import threading
import time

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50+1)
]


def craw_url(url):
    r = requests.get(url)
    # print(url, len(r.text))
    print(len(r.text))

craw_url(urls[0])

def single_craw():
    for url in urls:
        craw_url(url)


def multithread_craw():
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw_url, args=(url,))
        )

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

if __name__ == '__main__':
    print("开始单线程")
    start = time.time()
    single_craw()
    end = time.time()
    print("消耗的时间为： ", end - start, "秒")

print("开始多线程")
start = time.time()
multithread_craw()
end = time.time()
print("消耗的时间为： ", end - start, "秒")