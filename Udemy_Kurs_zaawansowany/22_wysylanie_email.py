# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 11:19:24 2023

@author: piter
"""
import smtplib

mailFrom = 'Wiadomosc testowa'
mailTo = ['piotrdomagala.wro@gmail.com', 'piotr.domagala@ue.wroc.pl']
mailSubject = 'Przetwarzanie zakończone powodzeniem!'
mailBody = '''Witaj,

Ta wiadomosć potwierdza, że wysyłanie e-maili za pomocą Pythona zakończyła się powodzeniem.
Nie musisz odpowiadać.'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'piterwroclaw@gmail.com'
password = 'xyzyzdcadada'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('Wiadomosc wysłana')
except:
    print('Błąd wysłania wiadomosci')
    