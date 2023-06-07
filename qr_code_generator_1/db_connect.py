import mysql.connector


class Connector:
    user_name="pavan"
    password="Pavan@123"
    host='localhost'

    def __init__(self):
        self.conn=mysql.connector.connect(
            host=self.host,
            user=self.user_name,
            password=self.password
        )

        self.cursor=self.conn.cursor()

        try:
            self.cursor.execute("""
            CREATE DATABASE IF NOT EXISTS qrcodedb;
            """)
            self.cursor.execute("""
            USE qrcodedb;
            """)

            print("SUCCESS :) qrcodedb is in use")
            self.conn.commit()

            
        
        except:
            print("ERROR :( while initializing db")

        else:
            print("Success :) db initialized and being used")

    def __repr__(self):
        return f"Database {self.conn}"
    
    def get_cursor(self):
        return self.cursor
    
    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()



if __name__=="__main__":
    mydb=Connector()
    print(mydb)
    cursor=mydb.get_cursor()
    print(cursor)
    mydb.commit()
    mydb.close()
