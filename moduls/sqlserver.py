import pyodbc

from datetime import date
import datetime


class SQLserver:
    '''Взаимодействие с БД'''

    def connect():
        '''Авторизация соединения с БД на удаленном сервере'''

        server = '####'
        database = '####'
        username = '####'
        password = '####'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
        return cnxn.cursor()

    def code_certificat():
        '''Получение и резервирование в системе свободного кода сертификата'''

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

        '''присвоение зарезервированому коду сертификата статуса занят'''
        SQLserver.update_status(code, 4)

        cursor.close()
        return res

    def update_status(code, status):
        '''Обновление статуса кода сертификата'''

        cursor = SQLserver.connect()
        cursor.execute(
            f"UPDATE CARD_CARDS SET status = {status} WHERE card_code  = {code}")
        cursor.commit()
        cursor.close()

    def update_data_code(code):
        '''
            Установление даты действия сертификата в 1 год с даты покупки
            Из за особенности обновления даты в БД SQL 2019 
            мы берем текущую дату и вычисляем разницу в днях с 1900-01-01
            прибавлем 1 год в днях и данное число передаем в обновления поля в БД
            получая обновления даты действия в один год с момента покупки
        '''

        today = date.today()
        endDate = date(today.year + 1, today.month, today.day)
        endDate = today.replace(today.year + 1)
        a = str(endDate)
        b = '1900-01-01'
        a = a.split('-')
        b = b.split('-')
        aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
        cc = aa-bb
        dd = str(cc)
        dddat = dd.split()[0]

        cursor = SQLserver.connect()
        cursor.execute(
            f"UPDATE CARD_CARDS SET exp_date = {dddat} WHERE card_code= {code} ")
        cursor.commit()
        cursor.close()

    def update_status_data(code, status):
        '''Получаем статус определённо кода сертификата'''

        cursor = SQLserver.connect()
        cursor.execute(
            f"UPDATE CARD_CARDS SET status = {status} WHERE card_code = {code}")
        cursor.commit()
        cursor.close()

        SQLserver.update_data_code(code)

    def code_reserv():
        '''Получаем все зарезервированные коды сертификатов'''

        cursor = SQLserver.connect()
        cursor.execute("SELECT card_code FROM card_cards "
                       "WHERE status = 4 AND card_code BETWEEN 400000 AND 400049")

        row = cursor.fetchone()
        tmp = list()

        while row:
            tmp.append(row[0])
            row = cursor.fetchone()

        cursor.close()

        return tmp

    def people_id(code):
        '''Получаем уникальный идентификатор кода сертификата'''

        cursor = SQLserver.connect()
        cursor.execute(
            f"SELECT people_id FROM card_cards WHERE card_code = {code}")

        row = cursor.fetchone()
        cursor.close()
        people_id = row[0]

        return people_id

    def update_balans(people_id, balans):
        '''Обновляем баланс карты пользователя после покупки сертификата''''

        cursor = SQLserver.connect()
        cursor.execute(
            f"SELECT TOP 1 PEOPLE_ACCOUNT_ID FROM CARD_PEOPLE_ACCOUNTS WHERE PEOPLE_ID = {people_id} AND BALANCE = 0")
        tmp = cursor.fetchone()
        cursor.close()

        cursor = SQLserver.connect()
        cursor.execute(
            f"UPDATE CARD_PEOPLE_ACCOUNTS SET BALANCE = {balans}  WHERE PEOPLE_ACCOUNT_ID = {tmp[0]} AND BALANCE = 0")
        cursor.commit()
        cursor.close()
