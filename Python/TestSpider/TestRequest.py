import requests

proxies = {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://www.baidu.com')
r = requests.get('https://www.google.com', proxies=proxies)
print(r.text)
