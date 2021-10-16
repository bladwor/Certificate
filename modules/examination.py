from . sqlserver import SQLserver
from . paykiper import Paykiper
from . qrcode import QRcode
from . smtpmail import Message


class Examination:
    '''
        Проверка платежей и зарезервированных кодов сертификата
        если зарезервированый код фигурирует в платежах то меняем статус на куплен 
        отсылаем письмо покупателю о покупке и сервисное письмо менеджеру.
        если зарезервированный код не фигурирует в платежной системе то меняем ему статус на свободен
    '''
    
    def update_status():
        '''обновление статуса'''

        code_reserv = SQLserver.code_reserv()
        last_order = Paykiper.last_order()

        for code in range(len(code_reserv)):
            for order in range(len(last_order)):
                if str(last_order[order]['orderid']) == str(code_reserv[code]):
                    if last_order[order]['status'] == 'success' and last_order[order]['status'] == 'stuck':
                        Examination.sert_update(code_reserv, last_order, order, code)
                    if last_order[order]['status'] == 'pending':
                        break
                    if last_order[order]['status'] == 'failed':
                        SQLserver.update_status(
                            last_order[order]['orderid'], 2)

        Examination.free_sert()

    def free_sert():
        '''Осбождение зарезервированных но не купленных кодов сертификата'''

        code_reserv_two = SQLserver.code_reserv()

        for code in code_reserv_two:
            SQLserver.update_status(code, 2)

    def sert_update(code_reserv, last_order, order, code):
        '''Проверка статуса'''

        SQLserver.update_status_data(last_order[order]['orderid'], 1)
        QRcode.touch_img_qr(last_order[order]['orderid'])

        people_id = SQLserver.people_id(code_reserv[code])

        SQLserver.update_balans(people_id, last_order[order]['pay_amount'])

        servise_name = Paykiper.servis_name(last_order[order]['id'])
        tmp = last_order[order]['pay_amount']
        price = tmp[:-3]

        Message.message_true(str(code_reserv[code]),
                             servise_name['service_name'],
                             str(last_order[order]['clientid']),
                             price,
                             servise_name['client_email']
                             )
        Message.message_true_service(str(code_reserv[code]),
                                     servise_name['service_name'],
                                     last_order[order]['clientid'],
                                     price,
                                     servise_name['client_email'],
                                     servise_name['client_phone'],
                                     )
