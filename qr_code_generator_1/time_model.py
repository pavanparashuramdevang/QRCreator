from db_connect import Connector


class Timestamp_table():

    def __init__(self):
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_timestamp_table()

    def create_timestamp_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS timestamp(
            qrData VARCHAR(255) NOT NULL,
            timestamp_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(qrData)
            );
            """)
            self.commit()
            print("SUCCESS :) timestamp data table is avilable")

        except:
            print("ERROR :( time stamp data table may already exists")

    
    def add_data(self,qr_data):
        sql=f"""
        INSERT INTO timestamp(qrData)
        VALUES ('{qr_data}');
        """
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connector.commit()
            print("qrdata added or updated")

        except:
            print("qrdata not ableto update/add ")

    def get_ten(self):
        sql="""
        SELECT * FROM data
        LIMIT 10;
        """
        try:
            self.cursor.execute(sql)
            data_val=self.cursor.fetchall()
            return data_val
        except:
            return None
        
    def close(self):
        self.connector.close()
        print("connection closed")

        
if __name__=="__main__":
    data=Data_table()
    data.add_data("ddifdjdafafaff ","dkjfadafiafn af")
    print(data.get_ten())
    data.close()
    
