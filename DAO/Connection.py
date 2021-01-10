from sqlobject.mysql import builder
import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class ConnectionManager:
    def __init__(self):
        self.user = 'YDA'
        self.passwd = 'ydayda'
        self.host = '175.24.35.47'
        self.db = 'YDA_RES'
        try:
            self.conn = builder()(user=self.user, password=self.passwd, host=self.host, db=self.db, charset="utf8mb4")
            self.conn.getConnection()
            self.is_connected = True
        except:
            print('建立连接失败')
            self.is_connected = False

    def connect_database(self):
        try:
            self.conn = builder()(user=self.user, password=self.passwd, host=self.host, db=self.db, charset="utf8mb4")
            self.conn.getConnection()
            self.is_connected = True
            return self.conn
        except:
            print('建立连接失败')
            self.is_connected = False

    def get_connection(self):
        return self.conn

    def get_connection_status(self):
        return self.is_connected

    def get_conn_info(self):
        return [self.user,
                self.passwd,
                self.host,
                self.db]

    def set_conn_info(self, new_user, new_passwd, new_host, new_database):
        if new_user is not None:
            self.user = new_user
        if new_passwd is not None:
            self.passwd = new_passwd
        if new_host is not None:
            self.host = new_host
        if new_database is not None:
            self.db = new_database
        self.connect_database()


base_conn = ConnectionManager()

"""
__uri = r'mysql://YDA:ydayda@175.24.35.47/YDA_RES?charset=utf8'
sqlhub.processConnection = connectionForURI(__uri)
"""
