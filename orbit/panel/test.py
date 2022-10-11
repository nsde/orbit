import proxy_list
import requests

proxy_list.update()

proxy = proxy_list.get()

print(proxy)
exit()
response = requests.get('https://api.ipify.org', proxies = {'https': proxy['address']})

print(response.text)