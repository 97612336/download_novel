# 得到待爬取的网址

# 解析网页内容

# 得到解析后的内容，存入数据库


# 开始爬取的url
# http://www.biquge.com.tw/1_1111/
import chardet
import requests

url = r"http://www.biquge.com.tw/1_1111/"

r = requests.get(url)

bytes_html = r.content

print(bytes_html)

res = chardet.detect(bytes_html)

encoding = res.get('encoding')

str_html = bytes_html.decode(encoding)

print(str_html)
