# -*- coding: utf-8 -*-

# -- Sheet --

'''
---------------------------- WSTĘP-----------------------------------------------


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
    ratio = float(input("Podaj nowe ratio: "))
    print(f"Ratio dla {myClient} wynosi {clients[myClient]}")
    print(f"Koszt dla {myClient} wynosi {ratio * totalCost}")
    print(f"Nowe ratio w porównaniu do starego: {clients[myClient]/ratio}")
except KeyError as e:
    print(f"Klienta {myClient} nie ma na liście {[c for c in clients.keys()]}.\n\nSzczegóły:{e}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Wystąpił problem z wartością ratio - podana wartość musi być typu liczbowego, różną od 0.\n\nSzczegóły:{e}")
#except ZeroDivisionError as e:
#   print(f"Nowa wartość ratio musi być różna od 0.\n\nSzczegóły: {e}")
except Exception as e:
    print(f"Mamy błąd...\nSzczegóły:\n{format(e)}")
'''

# ------------------------------------- ZADANIE ---------------------------------------------


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

except requests.exceptions.ConnectionError as e:
    print(f'Podany adres URL jest nieprawidłowy!\n')
    print(f'Szczegóły: {e}')

except PermissionError as e:
    print('Plik spis.html ma atrybut \"Tylko do odczytu\"\n')
    print(f'Szczegóły: {e}')

except FileNotFoundError as e:
    print(f'Nie istnieje plik download.tmp !\n')
    print(f'Szczegóły: {e}')

except Exception as e:
    print(f'Błąd!')
    print(f'Szczegóły błędu: {e}')

else:
    print(f'URL pobrany poprawnie {file}')

finally:
    if os.path.exists(tmpfile_path):
        print(f'Ostatecznie usuwamy plik {tmpfile_path}')
        os.remove(tmpfile_path) 
    print('ZADANIE ZAKOŃCZONE!')

