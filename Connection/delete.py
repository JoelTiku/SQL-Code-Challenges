
class DbDeleter:
    def __init__(self, conn, verbose=False):
        self.conn = conn
        self.verbose = verbose

    def delete(self):
        raise NotImplementedError


    def delete(self):
        conn = self.conn
        cursor = conn.cursor()

        cursor.execute(self.del_all_plsql)
        if self.verbose:
            print(f'Deleted all tables.')


class MySqlDeleter(DbDeleter):
    def delete(self):
        conn = self.conn
        cursor = conn.cursor(buffered=True)
        cursor.execute('SELECT DATABASE();')
        for result in cursor:
            db_name = result[0]

        cursor.execute(f"DROP DATABASE {db_name};")
        cursor.execute(f"CREATE DATABASE {db_name};")
        cursor.execute(f"USE {db_name};")
        conn.commit()

        if self.verbose:
            print(f'Deleted all tables from database {db_name}')
