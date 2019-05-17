import sqlite3
import src.constants as constants


class SQLHandler(object):
    def __init__(self):
        self.con = sqlite3.connect(constants.DATABASE_PATH, isolation_level=None)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        with open(constants.SCHEMA_PATH) as schema:
            self.cur.executescript(schema.read())

    @staticmethod
    def format_values(vals):
        values = vals
        for i in range(len(values)):
            if type(values[i]) == str:
                values[i] = "'{}'".format(values[i])
            values[i] = str(values[i])
        return ", ".join(values)

    def query(self, q):
        self.cur.execute(q)
        self.con.commit()

    def insert_row(self, table, column_list, value_list):
        columns = ", ".join(column_list)
        values = self.format_values(value_list)
        self.cur.execute("INSERT OR IGNORE INTO {0} ({1}) VALUES({2})".format(table, columns, values))
        self.con.commit()

    def insert_full_row(self, table, value_list):
        values = self.format_values(value_list)
        self.cur.execute("INSERT OR IGNORE INTO {0} VALUES({1})".format(table, values))
        self.con.commit()

    def get_row(self, table, column, value):
        self.cur.execute("SELECT * FROM {} WHERE {} = {}".format(table, column, value))
        return self.cur.fetchone()

    def get_rows(self, table, column, value):
        self.cur.execute("SELECT * FROM {} WHERE {} = {}".format(table, column, value))
        return self.cur.fetchall()

    def get_row_count(self, table):
        self.cur.execute("SELECT * FROM {}".format(table))
        return len(self.cur.fetchall())

    def delete_rows(self, table, conditional):
        self.cur.execute("DELETE FROM {} WHERE {}".format(table, conditional))
        self.con.commit()

    def update_row(self, table, update, conditional):
        self.cur.execute("UPDATE {0} SET {1} WHERE {2}".format(table, update, conditional))
        self.con.commit()

    def update_rows(self, table, update):
        self.cur.execute("UPDATE {0} SET {1}".format(table, update))
        self.con.commit()
