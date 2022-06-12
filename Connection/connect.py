import mysql.connector
from mysql.connector.cursor import MySQLCursor


class DbConnector:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        raise NotImplementedError


class MySqlConnector(DbConnector):
    def __init__(self, username, password):
        super(MySqlConnector, self).__init__(username, password)

    def connect(self):
        print('Connecting...')
        conn = mysql.connector.connect(host="localhost", user=self.username, passwd=self.password)
        print('Connection complete\n')
        return conn
