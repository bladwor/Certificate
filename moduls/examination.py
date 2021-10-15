from datetime import date

from blog.models import Post

from . sqlserver import SQLserver
from . paykiper import Paykiper
from . qrcode import QRcode
from . stmpmail import Message

import sys
import os


class Examination:
    def update_status():
        code_reserv = SQLserver.code_reserv()
        last_order = Paykiper.last_order()

        for code in range(len(code_reserv)):
            for order in range(len(last_order)):
                if str(last_order[order]['orderid']) == str(code_reserv[code]):
                    if last_order[order]['status'] == 'success':
                        SQLserver.update_status_data(last_order[order]['orderid'], 1)
                        QRcode.touch_img_qr(last_order[order]['orderid'])
                        people_id = SQLserver.people_id(code_reserv[code])
                        SQLserver.update_balans(people_id, last_order[order]['pay_amount'])
                        servise_name = Paykiper.servis_name(last_order[order]['id'])
                        Message.message_true(code_reserv[code],
                                             servise_name['service_name'],
                                             last_order[order]['clientid'],
                                             last_order[order]['pay_amount'],
                                             servise_name['client_email'],
                                             )
                        Message.message_true_service(code_reserv[code],
                                             servise_name['service_name'],
                                             last_order[order]['clientid'],
                                             (last_order[order]['pay_amount']),
                                             servise_name['client_email'],
                                             servise_name['client_phone'],
                                             )
                    if last_order[order]['status'] == 'pending':
                        break
                    if last_order[order]['status'] == 'failed':
                        SQLserver.update_status(last_order[order]['orderid'], 2)
                    if last_order[order]['status'] == 'stuck':
                        SQLserver.update_status_data(last_order[order]['orderid'], 1)
                        QRcode.touch_img_qr(last_order[order]['orderid'])
                        people_id = SQLserver.people_id(code_reserv[code])
                        SQLserver.update_balans(people_id, last_order[order]['pay_amount'])
                        servise_name = Paykiper.servis_name(last_order[order]['id'])
                        Message.message_true(code_reserv[code],
                                             servise_name['service_name'],
                                             last_order[order]['clientid'],
                                             last_order[order]['pay_amount'],
                                             servise_name['client_email'],
                                             )
                        Message.message_true_service(code_reserv[code],
                                             servise_name['service_name'],
                                             last_order[order]['clientid'],
                                             (last_order[order]['pay_amount']),
                                             servise_name['client_email'],
                                             servise_name['client_phone'],
                                             )
        code_reserv_two = SQLserver.code_reserv()

        for code in code_reserv_two:
            SQLserver.update_status(code, 2)
