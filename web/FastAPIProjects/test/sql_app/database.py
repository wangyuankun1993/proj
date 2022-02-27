from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://root:wangyuankun1993@localhost/fastapi?charset=utf8mb4")
# 创建引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# 声明基类
Base = declarative_base()
