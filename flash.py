import pymysql

db = pymysql.connect(host='localhost', user='root', password='xinfan1479496429', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS flash (title VARCHAR(1000) NOT NULL, text VARCHAR(8000) NOT NULL, PRIMARY KEY (title))'
cursor.execute(sql)
db.close()