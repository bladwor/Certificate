from django.test import TestCase

import pyodbc

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

        code = res[0]['card_code']
        print(code)

        cursor.execute(f"UPDATE CARD_CARDS SET status = 4 WHERE card_code  = {code}")

        cursor.close()

        return res
