import tornadoredis

c = tornadoredis.Client(host='127.0.0.1',port=6379)
# 测试是否连接成功，编写一个key，并查看Redis数据库是否存在该key
c.set("name","wangyuankun")
