import chardet
import requests


# 获取URL的网页HTML
def get_html_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__cdnuid=aba66920f28c86c961bbfb641ffe90d4; "
                  "PHPSESSID=7qfmgl8att4h60fpqf56kq6pv6; asdplan8718=1; dsa=1; asdplan9032=1",
        "Host": "http://www.biquge.com.tw",
        "Referer": "http://www.biquge.com.tw"
    }
    res = requests.get(url)
    html_bytes = res.content
    code_style = chardet.detect(html_bytes).get("encoding")
    html_text = html_bytes.decode(code_style, "ignore")
    return html_text
