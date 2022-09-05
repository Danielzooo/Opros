import smtplib
from email.mime.text import MIMEText
from inf import Info

email_sender = 'prostobotilinet@gmail.com'
password = 'dncinaqmgfnjlhmj'


smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(email_sender, password)


class Ml:
    @classmethod
    def send_mail(cls, mail):
        msg = MIMEText(f'Вы набрали {Info.points}/{len(Info.check)}')
        msg["Subject"] = 'Результаты теста'
        email_getter = mail
        smtp_server.sendmail(email_sender, email_getter, msg.as_string())
