from config.read_sql import get_mysql_db


# 保存书本信息到数据库
def save_book_info(one_book_dict):
    # 获取链接对象
    db = get_mysql_db()
    # 获取游标对象
    cursor = db.cursor()

    if not one_book_dict:
        return
    # 获取书名
    book_name = one_book_dict.get('name')
    # 获取书本的url
    book_url = one_book_dict.get('url')
    # 执行存入数据库的操作
    sql = r'INSERT into book (name,url) values("%s","%s");' % (book_name, book_url)
    try:
        cursor.execute(sql)
        db.commit()
        print("成功保存一本书")
    except:
        db.rollback()
        print("回滚一次")
