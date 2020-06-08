import pymysql
host = "localhost"
user = "jino"
password = "Password@123"
db = "jino"

# default null value  is enable below section


# db = None
# host = None
# user = None
# password = None


class Mysql_connection(object):
    def __init__(self, host=host, user=user, password=password, db=db):
        self.user = user
        self.password = password
        self.host = host
        self.db = db

    def open(self):
        try:
            connection = pymysql.connect(
                self.host, self.user, self.password, self.db)
            self.connection = connection
            self.session = connection.cursor()

        except pymysql.err.OperationalError as Error:
            print(Error)
            exit(0)

    def close(self):
        self.session.close()
        self.connection.close()

    def select(self, query):
        try:
            self.open()
            self.session.execute(query)
            result = self.session.fetchall()
            self.close()
            return result

        except pymysql.err.ProgrammingError as TableError:
            print(TableError)
            exit(0)

        except pymysql.err.InternalError as TableError:
            print(TableError)
            exit(0)


mysqlobject = Mysql_connection()

values = mysqlobject.select("SELECT * FROM test")
print(values)
