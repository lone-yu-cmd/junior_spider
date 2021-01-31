# 前三行存储
import requests

url = 'https://news.sina.com.cn/c/2021-01-31/doc-ikftpnny3010807.shtml'

res = requests.get(url)
res.encoding='UTF-8'
#print(res.encoding)

# content使用unicode 编码
# text 以程序认为可能的方式编码

f = open('testCreateFile.html', 'w+',encoding='UTF-8')

f.write(res.text)


f.close()
