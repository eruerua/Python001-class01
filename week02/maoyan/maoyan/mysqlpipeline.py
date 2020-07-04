import pymysql
 
 
class MysqlPipeline(object):
    """
    同步操作
    """
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='rootroot',db='test')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
 
    def process_item(self,item,spider):
        # sql语句
        insert_sql = "INSERT INTO MOVIES(TITLE, MTYPE, MTIME) VALUES ('%s', '%s',  '%s')" % (item['title'],item['mtype'],item['mtime'])
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql)
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
 
    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
