import pyodbc
from datetime import date
import datetime

class SQLserver:
    def connect():
        server = '89.221.58.60'
        database = 'Card_System'
        username = 'extcrm'
        password = 'Crm2020!'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return cnxn.cursor()

    def code_certificat():
        cursor = SQLserver.connect()

        cursor.execute("SELECT TOP 1 card_code, people_id, status FROM card_cards "
                       "WHERE status = 2 AND card_code BETWEEN 400000 AND 400049")

        row = cursor.fetchone()
        tmp = []

        while row:
            tmp.append(row)
            row = cursor.fetchone()

        keys = ['card_code', 'people_id', 'status']
        res = [dict(zip(keys, block)) for block in tmp]

        cursor.close()

        return res

    def update_status(code):
        cursor = SQLserver.connect()

        cursor.execute(f"UPDATE CARD_CARDS SET status = 4 WHERE card_code  = {code}")
        cursor.commit()
        cursor.close()

    def code_reserv():
        cursor = SQLserver.connect()
        cursor.execute("SELECT card_code FROM card_cards "
                       "WHERE status = 4 AND card_code BETWEEN 400000 AND 400049")

        row = cursor.fetchone()
        tmp = list()

        while row:
            #tmp.append(row)
            print(row[0])
            row = cursor.fetchone()

        return tmp

    def people_id(code):
        cursor = SQLserver.connect()
        cursor.execute(f"SELECT people_id FROM card_cards WHERE card_code = {code}")

        row = cursor.fetchone()
        cursor.close()
        people_id = row[0]
        return people_id

    def update_balans(code, balans):
        cursor = SQLserver.connect()
        cursor.execute(f"UPDATE CARD_CARDS SET status = 4 WHERE card_code  = {code}")
        cursor.commit()
        cursor.close()

    def update_data_code(code):
        today = date.today()
        endDate = date(today.year + 1, today.month, today.day)
        endDate = today.replace(today.year + 1)
        updatedata = f"{endDate} 00:00:00.000"
        a = str(endDate)
        b = '1900-01-01'
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
        cc = aa-bb
        dd = str(cc)
        dddat = dd.split()[0]
        cursor = SQLserver.connect()
        cursor.execute(f"UPDATE CARD_CARDS SET exp_date = {dddat} WHERE card_code= {code} ")
        cursor.commit()
        cursor.close()

SQLserver.update_data_code(400005)
