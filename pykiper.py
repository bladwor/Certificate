from http.client import HTTPConnection
from sys import argv, exit
from base64 import b64encode
from datetime import date

import urllib.request
import re, json, requests

class Paykiper:
    def last_order():
        REQUEST_URL = "/info/payments/search/"

        # Логин и пароль любого пользователя личного кабинета
        user = "admin"
        pw = "bd1853b412d1"
        # имя или IP-адрес вашего сервера с PayKeeper
        domain = "turandotpalace.server.paykeeper.ru"

        # В качестве аргумента скрипта указывается идентификатор платежа
        # (первый столбец в разделе "Платежи" личного кабинета PayKeeper)


        encstr = (user + ":" + pw).encode('ascii')
        hstr = b64encode(encstr).decode('ascii')

        try:
            pw
        except NameError:
            exit("domain not found!")
        else:
            print("Connecting...")

        headers = {'Authorization': 'Basic %s' % hstr}
        c = HTTPConnection(domain)
        c.request('GET', REQUEST_URL + "?query=&end_date=" + str(date.today()), headers=headers)
        res = c.getresponse()
        data = res.read().decode('ascii')

        if data == "":
            exit("No data!")

        data = json.loads(data)

        listen = []

        for item in range(0, 1):
            listen.append(data[item]['orderid'])

        #print(listen)
        return data[:1]

    def servis_name(id_order):
        REQUEST_URL = "/info/options/byid/"

        # Логин и пароль любого пользователя личного кабинета
        user = "admin"
        pw = "bd1853b412d1"
        # имя или IP-адрес вашего сервера с PayKeeper
        domain = "turandotpalace.server.paykeeper.ru"

        # В качестве аргумента скрипта указывается идентификатор платежа
        # (первый столбец в разделе "Платежи" личного кабинета PayKeeper)


        encstr = (user + ":" + pw).encode('ascii')
        hstr = b64encode(encstr).decode('ascii')

        try:
            pw
        except NameError:
            exit("domain not found!")
        else:
            print("Connecting...")

        headers = {'Authorization': 'Basic %s' % hstr}
        c = HTTPConnection(domain)
        c.request('GET', REQUEST_URL + "?id=" + str(id_order), headers=headers)
        res = c.getresponse()
        data = res.read().decode('ascii')

        if data == "":
            exit("No data!")

        data = json.loads(data)

        return data['service_name']

Paykiper.servis_name(33)
