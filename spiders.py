import pymysql

db = pymysql.connect(host='localhost', user='root', password='xinfan1479496429', port=3306)
cursor = db.cursor()
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()