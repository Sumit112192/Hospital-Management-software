import csv
from database import *
import getpass
#Hello, World I am Pranav I am new to python and I am trying to build this project with my basic knowledge in Python,

class Medicine:
    def __init__(self,company,expiry,name,price):
        self.company=company
        self.expiry=expiry
        self.name=name
        self.price=price

    def __str__(self):
        return f'Name:{self.name}\nCompany:{self.company}\nExpiry:{self.expiry}'

class Patient:
    def __init__(self,name,place,phone,age,visit):
        self.name=name
        self.place=place
        self.age=age
        self.phone=phone
        self.visit=visit


def register():
    pat_stat=input('Type y if patient is already registered else type n::')
    if pat_stat.lower() == 'n':
        name=input('Name:')
        place=input('Place:')
        age=input('Age:')
        phone=input('Phone:')
        visit=1
        pat=Patient(name,place,phone,age,visit)
        add_pt(pat)
        print('Patient registered')


    
    elif pat_stat.lower() == 'y':
        regno=input('Enter the registration number:')
        c=reg_no(regno)
        print(c)

       
    else:
        print('Enter y or n')

def issue_store(med,stock):
    rem_store(med,stock)
    add_pharma(med,stock)
    print('Medicine issued succesfully!!')


def billing(med,cfee):
    mrp=0
    if type(med) == type([]):
        for i in med:
            mrp+=i.price
    else:
        mrp=med.price
    return 'Name:\tPrice:\tConsultation Fee\tOverall:\n'+f'{med.name}\t{mrp}\t{cfee}\t{mrp+cfee}'

            
    
##########################################################
print('*'*100+'\n'+'Welcome to hospital management System'.center(100,'*')+'\n'+'*'*100)



        
        


        



