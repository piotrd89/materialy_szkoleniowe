# -*- coding: utf-8 -*-

# -- Sheet --
'''
WSTĘP


clients = {
    "INFO":0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER":0.1,
    "OMEGA": 0.0
}

myClient = input("Wprowadź imię klienta: ")
totalCost = 7200

try:
    print(f"Ratio dla {myClient} wynosi {clients[myClient]}")
except:
    print("Mamy błąd")
else:
    print(f"Koszt dla {myClient} wynosi {clients[myClient]*totalCost}")
finally:
    print("-Koniec obliczeń-")
'''

# =---------------ZADANIE-----------------------------------------------------------


import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/users/piter/kurs_zaawansowany'
tmpfile = 'download.tmp'
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print('usuwamy {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
        
    print('Pobieranie URL {}'.format(url))
    save_url_to_file(url, tmpfile_path)
    
    print('Kopiuje pliki {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print('Błąd pobierania URL {}'.format(url))
    print('Szczegóły błędu: {}'.format(e))

else:
    print('URL pobrany poprawnie {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Ostatecznie usuwamy plik {}'.format(tmpfile_path))
        os.remove(tmpfile_path) 
    print('UKOŃCZONE!')

