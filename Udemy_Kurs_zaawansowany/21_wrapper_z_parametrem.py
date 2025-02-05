# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:16:04 2023

@author: piter
"""

from datetime import datetime as dt
import functools #umożliwia stosowanie tzw. dekoratora
import os

# WSTĘP ----------------------------------------------
#logFilePath = r'C:\Users\piter\Kurs_zaawansowany\21_logi_wrapper.txt' scieżke bedziemy podawali jako paramter

def CreateFunctionWithWrapperLogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args,**kwargs):
            file = open(logFilePath,"a")
            file.write("-"*20 + "\n")
            file.write(f'START: {dt.now().isoformat()}\n')
            file.write(f'Wywoływana funkcja: {func.__name__} \n')
            file.write('Wykorzystane parametry: ')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}\n".format(k,v) for (k,v) in kwargs.items()))
            result = func(*args,**kwargs)
            file.write(f'WYNIK: {result}\n')
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapperLogToFile(r'C:\Users\piter\Kurs_zaawansowany\21_logi_bonusy.txt')
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print(f'Zmiana wypłaty dla {emp_name} jako bonus {new_salary} zł , a bonus= {is_bonus}')
    return new_salary

@CreateFunctionWithWrapperLogToFile(r'C:\Users\piter\Kurs_zaawansowany\21_logi_stanowiska.txt')
def ChangePosition(emp_name, new_position):
    print(f'Zmiana stanowiska {emp_name} na {new_position}')
    return new_position

#print(ChangeSalary('Kowalski', 20000, True))
#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)
#print(ChangePosition('Domagala','Dyrektor'))
#print(ChangeSalary('Domagala', 50000, is_bonus=True))

# ZADANIE ----------------------------------------------

def WrapperWithLogFile(logged_action, log_file_path):
    def WrapperWithLog(func):
        def wrapper(path):
            with open(log_file_path,'a') as f:
                f.write(f'Czas wykonania akcji: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\nAkcja {logged_action} wykonana na pliku {path}\n')
            return func(path)
        return wrapper
    return WrapperWithLog

@WrapperWithLogFile('FILE_CREATE', r'C:\Users\piter\Kurs_zaawansowany\21a_logi_file_create.txt')
def create_file(path):
    print(f'Tworzenie pliku {path}')
    open(path,"w+")

@WrapperWithLogFile('FILE_DELETE', r'C:\Users\piter\Kurs_zaawansowany\21a_logi_file_delete.txt')
def delete_file(path):
    print(f'Usuwanie pliku {path}')
    os.remove(path)

create_file(r'C:\Users\piter\Kurs_zaawansowany\dummy_file.txt')
delete_file(r'C:\Users\piter\Kurs_zaawansowany\dummy_file.txt')
create_file(r'C:\Users\piter\Kurs_zaawansowany\dummy_file.txt')
delete_file(r'C:\Users\piter\Kurs_zaawansowany\dummy_file.txt')