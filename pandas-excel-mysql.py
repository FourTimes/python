import pandas

class PandasExcelReader():
    def __init__(self, filename):
        self.filename = filename

    def Read(self):
        _target = pandas.read_excel(self.filename)
        t = []
        for i, j in _target.iterrows():
            serialNumber = i + 1
            name = j['NAME']
            _id = j['ID']
            _values = (serialNumber, name, _id)
            query = "INSERT INTO test (serial, name, id) values('%s', '%s', '%s')" % (
                _values)
            t.append(query)
        
        return t


import pymysql

def insert(query):
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='password',
                                    db='jjino',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = connection.affected_rows()

        return records

    except pymysql.err.DatabaseError as DatabaseError:
        print(DatabaseError)

    except pymysql.err.OperationalError as error:
        print("Error: {}".format(str(error)))
        
    finally:
        connection.close()

def select(query):
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='password',
                                    db='jino',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except pymysql.err.DatabaseError as DatabaseError:
        print(DatabaseError)

    except pymysql.err.OperationalError as error:
        print("Error: {}".format(str(error)))

    finally:
        connection.close()



result = PandasExcelReader('h.xlsx')
d = result.Read()
for i in d:
    insert(i)
