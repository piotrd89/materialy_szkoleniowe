# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:09:28 2023

@author: piter
"""

# WSTĘP -------------------------------------------------------
'''
dniPracujace = [19,21,22,21,20,22]
enumaratedDays = list(enumerate(dniPracujace))
print(enumaratedDays)

for pos, value in enumaratedDays:
    print('Pozycja: ', pos, 'Wartosc: ', value)
    
    
miesiace = ['I', 'II', 'III', 'IV', 'V', 'VI']

dniMiesiace = list(zip(miesiace, dniPracujace))
print(dniMiesiace)

for m,d in dniMiesiace:
    print('Miesiąc: ', m, 'Dni pracujących: ', d)
    
    
for pos, (m,d) in enumerate(zip(miesiace, dniPracujace)):
    print('Pozycja: ', pos, 'Miesiąc:', m, 'Dni Pracujących: ', d)
    
  '''  
# ZADANIE ------------------------------------------------------

projekty = ['Brexit','Nord Stream','US Mexico Border']
liderzy = ['Teresa May','Wladimir Putin','Bill CLinton & Donald Trump']
daty = ['2016-06-23','2016-08-29','1994-01-01']

liderzyProjektow = list(zip(projekty, liderzy, daty))

for p,l, d in liderzyProjektow:
    print("Liderem projektu ", p, "jest ", l,'. Projekt rozpoczął się w dniu: ', d)


print('Ponumerowawne projekty\n')
NrLiderzyProjektow = list(enumerate(liderzyProjektow))

for pos, (p,l,d) in NrLiderzyProjektow:
    print(pos+1,'. ', 'Projekt:', p, ', Lider projektu:', l, ', Data rozpoczęcia:', d)
