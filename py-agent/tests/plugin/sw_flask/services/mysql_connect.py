
import threading
import pymysql
from DBUtils.PooledDB import PooledDB
class MysqlTaskConfig(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        mysqlhost = "172.17.101.35"
        mysqlport = 4000
        mysqlusername = "cloudchain"
        mysqlpassword = "cloudchain123"
        mysqldatabase = "rkcc_srv_spider"
        try:
            self.pool = PooledDB(
                creator=pymysql,  # 使用链接数据库的模块
                maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
                maxshared=3,
                # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
                blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
                ping=0,
                # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
                host=mysqlhost,
                port=int(mysqlport),
                user=mysqlusername,
                password=mysqlpassword,
                database=mysqldatabase,
                charset='utf8mb4'
            )


            #self.conn = pymysql.connect(host=mysqlhost, port=int(mysqlport), user=mysqlusername, password=mysqlpassword,
            #                            database=mysqldatabase, charset="utf8mb4")
            #self.conn = self.pool.connection()
            #self.cursor = self.conn.cursor()
        except Exception as e:
            print("mysql写入错误:" + str(e))
            self.conn = ''
            self.cursor = ''

    @classmethod
    def get_instance(cls, *args, **kwargs):
        with MysqlTaskConfig._instance_lock:
            if not hasattr(MysqlTaskConfig, "_instance"):
                MysqlTaskConfig._instance = MysqlTaskConfig(*args, **kwargs)
        return MysqlTaskConfig._instance

    #读取爬虫日志

    #读取任务数据
    def mysql_data_read(self,sql):
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return cursor.fetchall()
        except:
            print("读取任务失败")

    #写入任务数据
    # status 1：运行 0：关闭

    def mysql_data_write(self,servername=[],data=[],createtime=[]):
        try:
            sql = 'insert into f_spider_data_test(f_servername,f_data,f_created_at) values(%s,%s,%s)'
            self.conn = self.pool.connection()
            self.cursor = self.conn.cursor()
            self.cursor.executemany(sql,servername)
            self.conn.commit()
        except Exception as e:
            print("task任务写入出错")



if __name__ == '__main__':
    mysql = MysqlTaskConfig()
    #result = mysql.mysql_task_get("中山市项目")
    result = mysql.mysql_task_compare()
    print()
