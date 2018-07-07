import chardet
import requests


# 获取URL的网页HTML
def get_html_text(url):
    res = requests.get(url)
    html_bytes = res.content
    code_style = chardet.detect(html_bytes).get("encoding")
    html_text = html_bytes.decode(code_style,"ignore")
    return html_text
