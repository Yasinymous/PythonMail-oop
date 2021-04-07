from .settings import SenderSettings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = SenderSettings

class SendMail:

    def baglan(self):
        sunucu = smtplib.SMTP_SSL(s.host, 465)
        sunucu.login(s.mail,s.password)
        return sunucu
    
    def mailgonder(self,to,subject,text,html):
        sunucu = self.baglan()
        gonderici = s.mail
        alici = to   
        msg = MIMEMultipart()
        msg['From'] = 'verification@yasinymous.com'
        msg['To'] = to
        msg['Subject'] = subject
        #msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        part1 = MIMEText(text, "plain", "utf-8")
        part2 = MIMEText(html, "html", "utf-8")
        msg.attach(part1)
        msg.attach(part2)
        try:

            sunucu.sendmail(gonderici,alici,msg.as_string())
            print("Mail başarılı bir şekilde gönderildi.")
        except EOFError:
            print("Mail gönderilirken hata oluştu.")
    
        sunucu.quit()
