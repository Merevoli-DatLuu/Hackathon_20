import mysql.connector

class db_connection:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.mydb =  mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = dbname
        )

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.dbname = 'hackathon'
        self.mydb =  mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.dbname
        )

    def query(self, query_str):
        """
        Hàm này dùng để truy vấn (select)
        :param: query_str => string
        :result: Table => list(tuple)
        """
        mycursor = self.mydb.cursor()

        mycursor.execute(query_str)

        myresult = mycursor.fetchall()

        mycursor.close()
        return myresult
    
    def insert(self, query_str, value):
        """
        Hàm này dùng để thêm(insert)
        :param: query_str => string
        :param: value => tuple
        :result: None
        """
        mycursor = self.mydb.cursor()

        mycursor.execute(query_str, value)

        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()

    def update(self, query_str):
        """
        Hàm này dùng để cập nhật(update)
        :param: query_str => string
        :result: None
        """
        mycursor = self.mydb.cursor()

        mycursor.execute(query_str)

        self.mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()

    def delete(self, query_str):
        """
        Hàm này dùng để xóa(delete)
        :param: query_str => string
        :result: None
        """
        mycursor = self.mydb.cursor()

        mycursor.execute(query_str)

        self.mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.close()

    def close(self):
        self.mydb.close()