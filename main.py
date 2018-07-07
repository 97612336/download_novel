from get_url.get_bigone_url import get_level_one_url

from parse_html.get_info import get_info_and_chapter_url

# 得到所有小说的大目录的url
big_one_url_list = get_level_one_url()
# 遍历所有的书本链接,进行具体的解析
for one in big_one_url_list:
    book_info = get_info_and_chapter_url(one)
    print(book_info)

# 根据所有小说的大URL获取小说所有章节的url



# 进行网页爬取，并得到网页爬取的内容

# 解析网页内容

# 得到解析后的内容，存入数据库


# 开始爬取的url
# http://www.biquge.com.tw/1_1001/
# 最后一篇文章
# http://www.biquge.com.tw/19_19767/
