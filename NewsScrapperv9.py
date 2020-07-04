import requests
from bs4
import BeautifulSoup
import urllib
import os
import img2pdf
from urllib.request
import urlopen
import datetime
from zipfile
import ZipFile
from PyPDF2
import PdfFileMerger

import smtplib
from email.mime.multipart
import MIMEMultipart
from email.mime.text
import MIMEText
from email.mime.base
import MIMEBase
from email
import encoders

from selenium
import webdriver
from selenium.webdriver.common.keys
import Keys
from selenium.webdriver.common.by
import By
import time

internet_date = urlopen('http://just-the-time.appspot.com/')
result = internet_date.read().strip()
result_str = result.decode('utf-8')
result_str = result_str.replace(' ', '-')
result_set = result_str.split('-')
final_date = result_set[2] + result_set[1] + result_set[0]

DayList = [
  'MON',
  'TUE',
  'WED',
  'THU',
  'FRI',
  'SAT',
  'SUN',
]
day_is = DayList[datetime.date(int(result_set[0]), int(result_set[1]),
  int(result_set[2])).weekday()]

i = 0
j = 1
c = 0

while j != 3:
  url = 'http://epaper.livehindustan.com/epaperimages/' + final_date\ +
  '/' + final_date + '-NGR-DDN-' + str(i) + str(j) + '.PDF'
h = requests.head(url, allow_redirects = True)
header = h.headers
content_type = header.get('content-type')

if 'application/pdf' in content_type.lower():
  print("Download start")
urllib.request.urlretrieve(url, 'local-filename' + str(i * 10 +
  j) + '.pdf')
j = j + 1
c = 0
else :
  c = c + 1
i = i + 1
j = 0

print('Downloads Completed.')

cwd = os.getcwd()
file_name = day_is.upper() + result_set[0] + result_set[1]\ +
  result_set[2]

merger = PdfFileMerger()
x = [a
  for a in os.listdir(cwd) if a.endswith(".pdf")
]

for pdf in x:
  merger.append(open(pdf, 'rb'))

with open(file_name + ".pdf", "wb") as fout:
  merger.write(fout)

driver = webdriver.Chrome(executable_path = r 'C:\Users\System32\Downloads\Compressed\chromedriver_win32_2\chromedriver')
driver.get("https://www.ilovepdf.com/compress_pdf")

input_tag = "//input[starts-with(@id,'html5_')]"
inputtag1 = "//input[starts-with(@id,'uploadfiles')]"

driver.find_element_by_xpath(input_tag).send_keys(cwd + r '/' + file_name + r '.pdf')
time.sleep(5)
print("done")
driver.find_element_by_id('uploadfiles').click()

comp_file = r "C:\Users\System32\Downloads\\" + file_name + r '-ilovepdf-compressed' + '.pdf'

while not os.path.exists(comp_file):
  time.sleep(1)

if os.path.isfile(comp_file):
  ZipFile(file_name + '.zip', 'w').write(comp_file)
ZipFile.close(ZipFile)
else :
  raise ValueError("%s isn't a file!" % comp_file)

# for i in os.listdir(cwd): #if i.endswith('.pdf'): #os.remove(i)

fromaddr = 'deeparshu5@gmail.com'
toaddr = 'atulbhatt98@gmail.com'
cwd = os.getcwd()

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'NEWS'

body = 'Hardwork'

msg.attach(MIMEText(body, 'plain'))

outfilename = file_name + '.zip'

file_to_open = os.path.join(cwd, outfilename)

attachment = open(file_to_open, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' %
  outfilename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, 'hypothetical')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()