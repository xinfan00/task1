import requests
import pymysql
from lxml import etree

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'}

url = 'https://www.8btc.com/flash'
# 响应的文本
data = requests.get(url, headers=headers).text
# 修正HTML的文本   输出<Element html at 0x1dae9f40e88>
s = etree.HTML(data)
# [<Element div at 0x1fcef3bbf88>]   [<Element div at 0x1cedfeebfc8>]
file = s.xpath('//*[@id="main"]/div/div/div[2]/div[5]/div[1]/div/div')

for div in file:
    # 创建列表用于存储爬取的数据
    flash = []
    # 获取标题，并将标题数据加入 list 列表
    title = div.xpath('./h6/a/p/text()')[0]
    # 获取text文本
    text = div.xpath('./div[1]/div/p/text()')[0]
    # 将text文本数据加入list列表
    flash.append([title, text])
    print(flash)

    # MYSQL
    # 1. 创建链接
    conn = pymysql.connect(
        host='localhost',  # 本地MYSQL
        user='root',  # 用户名
        password='xinfan1479496429',  # 密码
        port=3306,  # 端口号，默认
        db='spiders',  # 数据库名
        charset='utf8'  # 编码
    )
    # 2. 创建游标
    cur = conn.cursor()
    for l in flash:
        try:
            # 3. 传入参数, 执行命令
            cur.execute('insert into flash(title, text) values(%s, %s)', (l[0], l[1]))
            # 4. 数据插入 (提交至MySQL)
            conn.commit()
        except Exception as e:
            # 数据回滚
            conn.rollback()
    # 5. 关闭游标、连接
    cur.close()
    conn.close()