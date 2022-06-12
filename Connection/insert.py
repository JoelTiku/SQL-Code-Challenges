import json
import mysql.connector
from mysql.connector.cursor import MySQLCursor

class DbInserter:
    def __init__(self, conn, verbose=False):
        self.conn = conn
        self.verbose = verbose

    def insert(self, filepath, table_names=None, commit=True):
        raise NotImplementedError


class MySqlInserter(DbInserter):
    def insert(self, data, table_names=None, commit=True):
        conn = self.conn
        cursor = conn.cursor(buffered=True)

        tables_dict = data["tables"]

        # Insert table names based on order passed
        if table_names is None:
            table_names = list(tables_dict.keys())

        for table_name in table_names:
            rows = tables_dict[table_name]  # List of dictionary
            # Skip if any no values
            if len(rows) == 0:
                continue
            columns = [i for i in rows[0]]
            col_str = ','.join(sorted(rows[0].keys()))

            command1 = f'INSERT INTO {table_name}('
            command2 = ' VALUES ('
            for c in columns:
                command1 += f'{c},'
                command2 += f'%({c})s,'
            command1 = command1[:-1] + ')'
            command2 = command2[:-1] + ');'
            command = command1 + command2

            for row in rows:
                cursor.execute(command, row)

        if commit:
            conn.commit()
