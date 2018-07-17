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
    # 获取书本的封面图
    book_img = one_book_dict.get('img')
    # 获取书本的分类
    book_kind = one_book_dict.get("kind")
    # 获取书本的作者
    book_author = one_book_dict.get('author')
    # 执行存入数据库的操作
    sql = r'INSERT into book (name,url,book_img,kind,author) values("%s","%s","%s","%s","%s");' \
          % (book_name, book_url, book_img, book_kind, book_author)
    try:
        cursor.execute(sql)
        db.commit()
        print("成功保存一本书")
    except:
        db.rollback()
        print("回滚一次")
    cursor.close()
    db.close()


# 根据书名获取数据库中的id
def get_book_id_by_name(book_name):
    db = get_mysql_db()
    cursor = db.cursor()

    sql = 'SELECT id FROM book WHERE name="%s";' % book_name

    cursor.execute(sql)

    res = cursor.fetchone()

    cursor.close()
    db.close()

    if res:
        return res[0]
    else:
        return 0


# 根据book_id,查询数据库并更改has_chapter的值设为0
def set_book_has_chapter_by_id(book_id):
    db = get_mysql_db()
    cursor = db.cursor()
    sql = r'update book set has_chapter=0  where id=%s;' % book_id
    try:
        cursor.execute(sql)
        db.commit()
        print("成功设置has_chapter值")
    except:
        db.rollback()

    cursor.close()
    db.close()


# 根据one_chapter字典保存信息到chapter表中
def save_chapter(one_chapter):
    # 获取传值
    book_id = one_chapter.get("book_id")
    name = one_chapter.get("name")
    chapter_url = one_chapter.get("href")
    chapter_text = one_chapter.get('data')
    # 获取db
    db = get_mysql_db()
    cursor = db.cursor()
    sql = r"INSERT INTO chapter (book_id,name,chapter_url,chapter_text) VALUES(%s,'%s','%s','%s');" \
          % (book_id, name, chapter_url, chapter_text)
    try:
        cursor.execute(sql)
        db.commit()
        print("成功存储一个章节的内容")
    except:
        db.rollback()

    cursor.close()
    db.close()
