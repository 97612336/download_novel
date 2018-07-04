# 获取一级页面的url
def get_level_one_url():
    bigone_url_list = []
    for i in range(1, 20):
        half_url = r'http://www.biquge.com.tw/%s_%s' % (i, i)
        for j in range(1, 1000):
            if i == 19:
                if j < 768:
                    url = splicing_bigone_url(half_url, j)
                    bigone_url_list.append(url)
            else:
                url = splicing_bigone_url(half_url, j)
                bigone_url_list.append(url)
    return bigone_url_list


# 拼接一级页面URL
def splicing_bigone_url(half_url, j):
    str_num = str(j)
    len_num = len(str_num)
    if len_num == 1:
        str_num = "00" + str_num
    elif len_num == 2:
        str_num = "0" + str_num
    url = half_url + str_num + '/'
    return url


