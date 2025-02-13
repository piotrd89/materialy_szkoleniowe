# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:01:58 2023

@author: piter
"""

import types

'''

def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('To funkcja exportToFile - wersja statyczna')
    
def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('To funkcja exportToFile - metoda klasy')
      
def exportToFile_Instance(self,path):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('To funkcja exportToFile - metoda instancji')
    
    
Car.exportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.exportToFile_Class(path = r'C:\temp\export_Class.csv')
print(dir(Car))

car_01.exportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
Car.exportToFile_Instance(path = r'C:\temp\export_Instance.csv')
print(dir(car_01))

if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print("Obiekt posiada metodę ExportToFileStatic")


if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print("Obiekt posiada metodę ExportToFileStatic")
    

if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print("Obiekt posiada metodę ExportToFileStatic")
    
'''

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Rodzaj</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Smak</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Skladniki</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Wypelnienie</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

# METODA KLASY -------------------------------------
    
def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data="""
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Rodzaj</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Smak</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Skladniki</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Wypelnienie</td>
         <td>{}</td>
       </tr>"""
    template_footer="""</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)

# METODA INSTANCJI -------------------------------------

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Rodzaj</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Smak</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Skladniki</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Wypelnienie</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

# DEFINICJA KLASY --------------------------------------
class Cake:
 
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
 
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)
 
    def set_filling(self, filling):
        self.filling = filling
 
    def add_additives(self, additives):
        self.additives.extend(additives)
 
    def __get_text(self):
        return __text
 
    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))
 
    Text = property(__get_text, __set_text, None, 'Text on the cake')
 
 
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')

#Metoda statyczna:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, r'C:\Users\piter\Kurs_zaawansowany\34_dynamiczne_metody\statycznie.html')

#Metoda klasy:
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html(r'C:\Users\piter\Kurs_zaawansowany\34_dynamiczne_metody\class_method.html')

#Metoda instancji:
for c in Cake.bakery_offer:
    c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
    c.export_this_cake_to_html(r'C:\Users\piter\Kurs_zaawansowany\34_dynamiczne_metody\{}.html'.format(c.name.replace(' ','_')))