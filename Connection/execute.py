import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import errorcode


class Executor:
    def __init__(self, conn, verbose=False):
        self.conn = conn
        self.verbose = verbose

    def execute(self, filepath, commit):
        raise NotImplementedError



class MySqlExecutor(Executor):
    def execute(self, filepath, commit=True):
        conn = self.conn
        cursor = conn.cursor(buffered=True)

        with open(filepath) as f:
            file = f.read()

        for block in file.split(';'):
            block = block.strip()

            # Skip empty command
            if block == '':
                continue

            # Remove comment from lines
            lines = block.split('\n')
            block = '\n'.join([i for i in lines if not (i.strip().startswith('--') or i == '')])

            try:
                cursor.execute(block)
            except mysql.connector.Error as exception:
                self._handle_exception(exception, block)

        if commit:
            conn.commit()

    @staticmethod
    def _handle_exception(exception, block):
        # Allow unknown table for drop command
        if exception.errno == errorcode.ER_BAD_TABLE_ERROR and 'drop' in block:
            return

        print(f'{"-"*70}\n>>> EXCEPTION OCCURRED FOR COMMAND :-\n{block}')
        print(f'\n>>> EXCEPTION MESSAGE :-\n{exception}')
        print('\n\nEXIT WITHOUT COMPLETING !')

        sys.exit(-1)
