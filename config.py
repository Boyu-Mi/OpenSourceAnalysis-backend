# 设置连接数据库的URL
user = 'root'
password = '12345'
database = 'sre'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user,password,database)

# 设置sqlalchemy自动跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = False

# 禁止自动提交数据处理
SQLALCHEMY_COMMIT_ON_TEARDOWN = False

