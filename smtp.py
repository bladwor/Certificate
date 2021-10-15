from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import email.message


class Message:
    def messages(code, name_cert, name, price, mail):
        # create message object instance
        msg = MIMEMultipart()
        
        # setup the parameters of the message

        text = ("<div style=\"max-width:500px; margin: 0 auto; background: #f6f6f7; border-radius: 15px; padding: 15px;\">"
                "<div style=\"text-align: center\">"
                "<img src=\"https://s724266.sendpul.se/image/files/emailservice/userfiles/7fe1680e18920d765262308f17943b08724266/TVR/TURANDOT_LOGO__NEW_-_kopiya.png\" >"
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
                f"<img src=\"https://turandotpalace.ru/qrimg/{code}.png\" alt="" style=\"width:100%\">"
                "</div>"
                "<hr>"
                "<h1 style=\"text-align: center; color: #524f4f;\">turandotpalace</h1>"
                "<p>"
                  "Вы получили это письмо, потому что выразили свое согласие получать сообщения от turandotpalace."
                " Если Вы хотите отказаться от получения писем, <a href=\"#\">нажмите здесь</a>."
                "</p>"
                "</div>")
        email_content ='<html><head></head><body><p>' + text + '</p></body></html>'

        msg = email.message.Message()
        msg['Subject'] = 'Tutsplus Newsletter'
        
        
        msg['From'] = "hostmaster@turandot-palace.ru"
        msg['To'] = mail
        password = "ERqomcPr2njK8X"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        
        #create server
        s = smtplib.SMTP('smtp-pulse.com:587')
        s.starttls()
        
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        print ("successfully sent email to %s:" % (msg['To']))


#code, name_cert, name, price, mail
code = 400009
name_cert = 'Бранч на покупку Алкоголя'
name = 'Вронов Дмитрий'
price = 25000
mail = 'dmitriy.woronow@gmail.com'

Message.messages(code, name_cert, name, price, mail)


