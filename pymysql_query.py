import pymysql

def insert(query):
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='password',
                                    db='jino',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = connection.affected_rows()
        connection.close()

        return records

    except pymysql.err.DatabaseError as DatabaseError:
        print(DatabaseError)

    except pymysql.err.OperationalError as error:
        print("Error: {}".format(str(error)))

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
        connection.close()
        return result

    except pymysql.err.DatabaseError as DatabaseError:
        print(DatabaseError)

    except pymysql.err.OperationalError as error:
        print("Error: {}".format(str(error)))


# Call INSERT FUNCTION

insert_details = insert("INSERT INTO details (id, name) VALUES (2, 'JOE JINO')")
print("Number of records inserted: {}".format(insert_details))


select_details = select('SELECT * FROM details')

for details in select_details:
    print(details)