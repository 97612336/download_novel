import datetime
import time

from get_url.get_bigone_url import get_level_one_url, get_chapter_by_book_info

from parse_html.get_info import get_info_and_chapter_url
from save_to_db.save_book import save_book_info

# 得到所有小说的大目录的url
big_one_url_list = get_level_one_url()
# 遍历所有的书本链接,进行具体的解析
for one in big_one_url_list:
    # 记录开始时间
    start_time = time.time()
    print(one)
    # 获取书本的书本名\所有章节名和章节url
    try:
        book_info = get_info_and_chapter_url(one)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
        continue
    # 如果没有获取到书本信息,则直接退出本次循环
    if not book_info:
        print(datetime.datetime.now())
        print("没有书本信息,退出本次循环")
        continue
    # 执行存入数据库的操作
    is_success = save_book_info(book_info)
    # 如果保存书名的时候出错,直接退出本次循环
    if not is_success:
        print(datetime.datetime.now())
        print("保存数据库失败,退出本次循环")
        continue
    # 根据book_info,得到所有章节,然后存入到数据库中
    get_chapter_by_book_info(book_info)

    # 记录结束时间
    end_time = time.time()
    cost_time = end_time - start_time
    print(datetime.datetime.now())
    print("本次执行共花费了%s秒" % cost_time)


