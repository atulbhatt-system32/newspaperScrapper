import requests
from bs4 import BeautifulSoup
import urllib
import os
from urllib.request import urlopen
import datetime
from zipfile import ZipFile
from PyPDF2 import PdfFileMerger
import img2pdf
import sys, math, random
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5.QtGui import QPainter, QPen, QColor, QKeySequence
from PyQt5.QtCore import Qt, QTimer, QThread

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ctypes

def auto(quality, email, self):
    internet_date = urlopen('http://just-the-time.appspot.com/')
    result = internet_date.read().strip()
    result_str = result.decode('utf-8')
    result_str = result_str.replace(' ', '-')
    result_set = result_str.split('-')
    final_date = result_set[2] + result_set[1] + result_set[0]
    cwd = os.getcwd()
		
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
    download_Counter = 0
    extension = ""
    percentage_Download = 0


    static_url =  'http://epaper.livehindustan.com/epaperimages/' + final_date \
            + '/' + final_date

   
    static_url = static_url+'-ng1r-del-'
    extension = ".jpg"   

    while c != 2:
        QApplication.processEvents()
        url =  static_url + str(i) + str(j) + extension
        h = requests.head(url, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        if(quality):

            if 'image/jpeg' in content_type.lower():

                urllib.request.urlretrieve(url, 'local-filename' + str(i * 10
                                           + j) + '.jpeg')
                j = j + 1
                c = 0
                download_Counter = download_Counter + 1
                percentage_Download = (download_Counter/26)*100
                self.pbar.setValue(percentage_Download)
                print(str(int(percentage_Download)) + "% Downloaded.")

            else:
                c = c + 1
                i = i + 1
                j = 0
       

    print ('Downloads Completed.')
    self.pbar.setValue(100)
	

    file_name = day_is.upper()+result_set[0]+result_set[1]+result_set[2]
    with open(file_name+".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir(cwd) if i.endswith(".jpeg")]))


    for i in os.listdir(cwd):
        if i.endswith('.jpeg'):
            os.remove(i)

            
    comp_file = file_name + '.pdf'

    while not os.path.exists(comp_file):
        time.sleep(1)

    if os.path.isfile(comp_file):
        ZipFile(file_name + '.zip', 'w').write(comp_file)
        ZipFile.close(ZipFile)
    else:
        raise ValueError("%s isn't a file!" % comp_file)



    fromaddr = 'Enter an email adress to send.'
    toaddr = email
    cwd = os.getcwd()

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'NEWSPAPER for' + day_is

    body = 'Download the file and uncompress it. Read and Enjoy.'

    msg.attach(MIMEText(body, 'plain'))

    outfilename = file_name + '.zip'

    file_to_open = os.path.join(cwd, outfilename)

    attachment = open(file_to_open, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s'
                    % outfilename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'enter_password')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

