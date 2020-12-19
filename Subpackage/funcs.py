from  database import *


# Hello, World I am Pranav I am new to python and I am trying to build this project with my basic knowledge in Python,





class Medicine:
    def __init__(self, company, expiry, name, price):
        self.company = company
        self.expiry = expiry
        self.name = name
        self.price = price

    def __str__(self):
        return f'Name:{self.name}\nCompany:{self.company}\nExpiry:{self.expiry}'


class Patient:
    def __init__(self, name, place, phone, age, visit):
        self.name = name
        self.place = place
        self.age = age
        self.phone = phone
        self.visit = visit


def register():
    pat_stat = input(
        "Press 'n' for registering new patient\nPress 'r' for re-visit ")
    if pat_stat.lower() == 'n':
        name = input('Name:')
        place = input('Place:')
        age = input('Age:')
        phone = input('Phone:')
        visit = 1
        pat = Patient(name, place, phone, age, visit)
        add_pt(pat)
        print('Patient registered')

    elif pat_stat.lower() == 'r':
        regno = input('Enter the registration number:')
        c = reg_no(regno)
        print(c)

    else:
        print('Enter y or n')


def stock_ex(med, stock):
    rem_store(med, stock)
    add_pharma(med, stock)
    print('Medicine issued succesfully!!')


def billing(med, cfee):
    mrp = 0
    if type(med) == type([]):
        for i in med:
            mrp += i.price
    else:
        mrp = med.price
    return 'Name:\tPrice:\tConsultation Fee\tOverall:\n'+f'{med.name}\t{mrp}\t{cfee}\t{mrp+cfee}'


def med_stor():
    n = input('Enter name of medicine(in lowercase)::')
    c = input('Enter company::')
    e = input('Enter Expiry date (in dd/mm/yy format)::')
    p = input('Enter price::')
    c = Medicine(c, e, n, p)
    return c


def ex_prompt():

    n = input('Enter name of the medicine\n::')
    med = med_search(n)
    stock = int(input('Enter stock quantity\n::'))
    stock_ex(med, stock)
    r = input("Press t to do again\nOr press p to go back\nPress x to exit::")

    if r.lower() == 't':
        return ex_prompt()
    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0


def vstore_prompt():
    s=view_store()
    print(s)
    r = input("Press 't' to do again\nOr press 'p' to go back\nPress 'x' to exit::")

    if r.lower() == 't':
        return vstore_prompt()

    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0


def add_prompt():
    med = med_stor()
    stock = int(input('Enter stock quantity\n::'))
    add_store(med, stock)
    r = input("Press 't' to add more\nOr press 'p' to go back\nPress 'x' to exit::")

    if r.lower() == 't':
        return add_prompt()
    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0


def vpharm_prompt():
    v=view_pharma()
    print(v)
    r = input("Press 't' to do again\nOr press 'p' to go back\nPress 'x' to exit::")

    if r.lower() == 't':
        return vpharm_prompt()

    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0


def ipharm_prompt():
    n = input('Enter medicine name\n::')
    med = med_search(n)
    stock = int(input('Enter amount::'))
    pharma_issue(med, stock)
    r = input("Press 't' to do again\nOr press 'p' to go back\nPress 'x' to exit::")

    if r.lower() == 't':
        return ipharm_prompt()

    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0


def pr_prompt():
    s=pat_list()
    print(s)
    
    r = input("Press 't' to do again\nOr press 'p' to go back\nPress 'x' to exit::")

    if r.lower() == 't':
        return pr_prompt()

    elif r.lower() == 'p':
        # return one to continue
        return 1
    elif r.lower() == 'x':
        print("exiting...")
        # and zero to break
        return 0

   


def bill_prompt():
    print('This Feature will be coming soon')


##########################################################
print('*'*100+'\n'+'Welcome to hospital management System'.center(100, '*')+'\n'+'*'*100)

on = True
while on:
    select = input("Enter 'o' Outpatient\nEnter 's' for Managing store\nEnter 'p' for managing pharmacy\nEnter 'r' for viewing patient records Enter 'b' for billing\n::")
    if select.lower() == 'o':
        register()
    elif select.lower() == 's':
        s = input("Press 'v' to view current medicine stock\nPress 'e' to execute stock exchange\nPress 'a' to add medicine to store\n::")
        if s.lower() == 'v':
            res = vstore_prompt()
            if res == 1:
                continue
            elif res == 0:
                break
        elif s.lower() == 'e':
            res = ex_prompt()
            if res == 1:
                continue
            elif res == 0:
                break
        elif s.lower() == 'a':
            res = add_prompt()
            if res == 1:
                continue
            elif res == 0:
                break

    elif select.lower() == 'p':
        s = input(
            "Press 'v' to see current stock in pharmacy\nPress 'i' to issue medicine from pharmacy\n::")
        if s.lower() == 'v':
            v=vpharm_prompt()
            if v==1:
                continue
            elif v==0:
                break
        elif s.lower() == 'i':
            i=ipharm_prompt()
            if v==1:
                continue
            elif v==0:
                break

    elif select.lower() == 'r':
        pat=pr_prompt()
        if pat == 1:
            continue
        elif pat == 0:
            break
        

    elif select.lower() == 'b':
        bill_prompt()
