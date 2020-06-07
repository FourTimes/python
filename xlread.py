import pymysql
import xlrd

host     = "localhost"
password = "password"
db       = "jino"
user     = "root"


def insert(query, values):
    try:
        connection = pymysql.connect(host,
                                     user,
                                     password,
                                     db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        records = connection.affected_rows()

        return records

    except pymysql.err.DatabaseError as DatabaseError:
        print(DatabaseError)

    except pymysql.err.OperationalError as error:
        print("Error: {}".format(str(error)))

    finally:
        connection.close()


book = xlrd.open_workbook("h.xlsx")
sheet = book.sheet_by_name("Sheet1")

query = """INSERT INTO details (id, name) VALUES (%s, %s)"""

for r in range(1, sheet.nrows):
    _id = sheet.cell(r, 0).value
    name = sheet.cell(r, 1).value
    values = (_id, name)
    insert(query, values)


# CREATE database jino;
# CREATE TABLE details (id int, name varchar(255))
