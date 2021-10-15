import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

class Message:
    def message_true(code, name_cert, name, price, mail):
        server = 'smtp-pulse.com'
        user = 'hostmaster@turandot-palace.ru'
        password = 'ERqomcPr2njK8X'

        recipients = str(mail)
        sender = 'hostmaster@turandot-palace.ru'
        subject = f'{name_cert}'
        text = ("<div style=\"max-width:500px; margin: 0 auto; background: #f6f6f7; border-radius: 15px; padding: 15px;\">"
                "<div style=\"text-align: center\">"
                 " <img src=\"https://s724266.sendpul.se/image/files/emailservice/userfiles/7fe1680e18920d765262308f17943b08724266/TVR/TURANDOT_LOGO__NEW_-_kopiya.png\" >"
                "</div>"
                "<hr>"
                f"<h2 style=\"text-align: center; color: #524f4f;\">{name}, поздравляем! <br></h2>"
                f"Вы приобрели {name_cert} №{code} номиналом {price} руб. <br>"
                "Вы можете воспользоваться им в течение года с момента покупки (<a href=\"https://turandotpalace.ru/politic/\">условия покупки и использования</a>).<br>"
                "При посещении ресторана предъявите персоналу QR-code (куаркод). <br> <br>"
                "С нетерпением ждем вас в гости! <br>"
                "Не забудьте предварительно забронировать стол. <br><br>"
                "С уважением, команда ресторана «Турандот» <br>"
                "Москва, Тверской бульвар, 26 <br>"
                "welcome@turandot-palace.ru <br>"
                "+7 (495) 739-00-11 <br>"
                "<div style=\"text-align: center\">"
                f"  <img src=\"https://turandotpalace.ru/qrimg/{code}.png\" alt="" style=\"width:100%\">"
                "</div>"
                "<hr>"
                "<h1 style=\"text-align: center; color: #524f4f;\">turandotpalace</h1>"
                "<p>"
                  "Вы получили это письмо, потому что выразили свое согласие получать сообщения от turandotpalace."
                 " Если Вы хотите отказаться от получения писем, <a href=\"#\">нажмите здесь</a>."
                "</p>"
                "</div>")
        html = '<html><head></head><body><p>' + text + '</p></body></html>'

        filepath = f"{code}.png"
        basename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'turandotpalace.ru <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')
        part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
        part_file.set_payload(open(filepath, "rb").read())
        part_file.add_header('Content-Description', basename)
        part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
        encoders.encode_base64(part_file)

        msg.attach(part_text)
        msg.attach(part_html)
        msg.attach(part_file)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()

    def message_true_service(code, name_cert, clientid, price, mail, phone):
        server = 'smtp-pulse.com'
        user = 'hostmaster@turandot-palace.ru'
        password = 'ERqomcPr2njK8X'
	
        tyuiop = str(mail)
        recipients = ['welcome@turandot-palace.ru']
        sender = 'hostmaster@turandot-palace.ru'
        subject = f'Приобретен {name_cert} №{code}'
        text = (f"Был приобретен {name_cert} №{code} номиналом {price} руб. <br>"
                f"Данные покупателя: <br>"
                f"{clientid} <br>"
                f"{phone} <br>"
                f"{mail} <br>")
        html = '<html><head></head><body><p>' + text + '</p></body></html>'

        # filepath = f"{code}.png"
        # basename = os.path.basename(filepath)
        # filesize = os.path.getsize(filepath)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'turandotpalace.ru <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')
        # part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
        # part_file.set_payload(open(filepath, "rb").read())
        # part_file.add_header('Content-Description', basename)
        # part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
        # encoders.encode_base64(part_file)

        msg.attach(part_text)
        msg.attach(part_html)
        #msg.attach(part_file)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        
    def message_test(code, name_cert, name, price, mail):
        server = 'smtp-pulse.com'
        user = 'hostmaster@turandot-palace.ru'
        password = 'ERqomcPr2njK8X'
	
        tyuiop = str(mail)
        recipients = 'welcome@turandot-palace.ru'
        sender = 'hostmaster@turandot-palace.ru'
        subject = f'{name_cert}'
        text = ("test")
        html = '<html><head></head><body><p>' + text + '</p></body></html>'

        filepath = f"{code}.png"
        basename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'turandotpalace.ru <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')
        part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
        part_file.set_payload(open(filepath, "rb").read())
        part_file.add_header('Content-Description', basename)
        part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
        encoders.encode_base64(part_file)

        msg.attach(part_text)
        msg.attach(part_html)
        msg.attach(part_file)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
