# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 11:36:22 2023

@author: piter
"""

import smtplib, functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}

    {}
    '''.format(mailFrom,mailSubject,mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user,password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('Wiadomosc wysłana')
        return True
    except:
        print('Błąd wysłania wiadomosci')
        return False

mailFrom = 'Wiadomosc testowa'
mailTo = ['piotrdomagala.wro@gmail.com', 'piotr.domagala@ue.wroc.pl']
mailSubject = 'Przetwarzanie zakończone powodzeniem!'
mailBody = '''Witaj,

Ta wiadomosć potwierdza, że wysyłanie e-maili za pomocą Pythona zakończyła się powodzeniem.
Nie musisz odpowiadać.'''

user = 'piterwroclaw@gmail.com'
password = 'Suszarka100%'

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject = 'POwiadomienie o wykonaniu funkcji')
  
SendInfoEmailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody)
        
#SendInfoEmail(user,password, mailFrom, mailTo, mailSubject, mailBody)