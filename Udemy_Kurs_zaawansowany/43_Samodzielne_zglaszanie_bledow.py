# -*- coding: utf-8 -*-

# -- Sheet --

'''
----------------------------- WSTĘP -------------------------------------------


def ProcessInvoice(n,b):
    if n >= b:
        raise ValueError("Wartość netto  powinna być niższa niż brutto!")
    else:
        print(f"Przetwarzanie faktury: netto={netto} brutto={brutto}")

def EndOfMonth():
    
    netto = 1230
    brutto = 1000

    try:
        ProcessInvoice(netto,brutto)
        1/0
    except ValueError as e:
        print(f"Wartości na fakturze są niepoprawne: {e}")
        raise ValueError('Błąd podczas przetwarzania faktur') from e
    except Exception as e:
        print(f"Błąd przetwarzania faktury: {e}")
        raise Exception('Błąd ogólny')

EndOfMonth()
'''
# ----------------------------- ZADANIE -------------------------------------------


import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Pusty tytuł!")
        if self.start > self.end:
            raise ValueError("Data początkowa jest większa od daty końcowej!")
    
    @classmethod    
    def publish_offer(cls,list_of_trips):
        list_of_errors=[]
        
        for t in list_of_trips:
            try:
                t.check_data()
            except ValueError as e:
                list_of_errors.append(f"{t.symbol}: {str(e)}")
            except Exception as e:
                list_of_errors.append(f"{t.symbol}: {str(e)}")

        if len(list_of_errors) > 0:
            raise Exception(f"Lista błędów: {list_of_errors}")
        else:
            print('Oferta zostanie opublikowana wkrótce...')


 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]


try:
    print('Publikowanie oferty wycieczek...')
    Trip.publish_offer(trips)
    print('... ukończone')
except Exception as e:
    print('WYSTĘPUJĄ BŁĘDY')
    print(e)
    print('OFERTA NIE MOŻE ZOSTAĆ OPUBLIKOWANA')
    





