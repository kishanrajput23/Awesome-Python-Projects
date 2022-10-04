import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

content=''

def extract_news(url):
    print('Extracting Hacker News Strories')
    cnt=''
    cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.paerser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt+=((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
    return(cnt)

cnt= extract_news('https://news.vcombinator.com/')
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Message')

print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'your email id'
TO = 'to email id'
PASS = 'your email password '

msg= MIMEMultipart()

msg['Subject']='topnews stories HN [mail] ' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From']= FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
print('Initating server...')

server = smtplib.SMTP(SERVER, PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('email sent...')

server.quit()
