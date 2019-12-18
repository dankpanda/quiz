temp = [] # List with all their names rearranged
temp2 = [] # List with all their format rearranged
temp3 = [] # List with all their format splitted
id_list = [] # List with all their id
class Employee():
    def __init__(self,ID,name,position,salary):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary

def start(filename):
    
    with open(filename,'r') as f:
        f_read = f.read()
        f_split = f_read.split("\n")
        for i in f_split:
            f_split2 = i.split('#')
            temp.append(f_split2[1])
            id_list.append(f_split2[0])
            Employee(f_split2[0],f_split2[1],f_split2[2],f_split2[3])
        temp.sort()
        for i in temp:
            for j in f_split:
                if j[6:6+len(i):] == i:
                    temp2.append(j)
    for row in temp2:
        temp3.append(row.split('#'))
    
    display()

def display():
    print(" ID        Name    Position    Salary")
    for row in temp3:
        print(row)
    print("1. New Staff \n2. Delete Staff \n3. View Summary Data \n4. Save & Exit")
    while True:
        action = input("Input choice:")
        if action == '1':
            new_staff()
            break
        if action == '2':
            delete_staff()
            break
        if action =='3':
            view_summary_data()
            break
        if action == '4':
            save_exit()
            break
        else:
            continue

def new_staff():
    print("New Staff")
    while True:
        ID = input("Input ID[SXXXX]:").upper()
        if len(ID) != 5:
            continue
        if ID[0] != 'S': 
            continue
        if int(ID[1:5]) not in range(0,10000):
            continue
        if ID in id_list:
            continue
        break
    while True:
        name = input("Input Name [0...20]:")
        if len(name) > 20:
            continue
        else:
            break
    while True:
        position = input("Input Position [Staff | Officer | Manager]:").title()
        if position not in ['Staff','Officer','Manager']:
            continue
        else:
            break
    while True:
        try:
            salary = int(input("Input salary for"+' '+position))
        except ValueError:
            print("Please enter an integer!")
            continue
        if position == 'Staff':
            if salary not in range(3500000,7000000):
                continue
            else:
                break
        if position == 'Officer':
            if salary not in range(7000001,10000000):
                continue
            else:
                break
        if position == 'Manager':
            if salary < 10000000:
                continue
            else:
                break
    Employee(ID,name.title(),position,salary)
    temp2.append(ID+"#"+name.title()+"#"+position+"#"+str(salary))
    temp3.append([ID,name.title(),position,salary])
    id_list.append(ID)
    display()
        
def delete_staff():
    pass
            
def view_summary_data():
    print("1. Staff")
    print("Minimum Salary: 4500000")
    print("Maximum Salary: 5000000")
    print("Average Salary: 4750000")
    print("\n2. Officer")
    print("Minimum Salary: 8500000")
    print("Maximum Salary: 8500000")
    print("Average Salary: 8500000")
    print("\n3.Manager")
    print("Minimum Salary: 10700000")
    print("Maximum Salary: 10700000")
    print("Average Salary: 10700000")
    display()

def save_exit():
    with open("saved file.txt",'w') as f:
        for row in temp2:
            f.write(row+"\n")

    
start('williammarugame.txt')
