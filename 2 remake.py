from statistics import mean

class Employee():
    id_list = []
    name_list = []
    new_list = []
    salary_list = []
    staff_salary = []
    officer_salary = []
    manager_salary = []
    
        
    def __init__(self):
        with open("test.txt",'r') as f:
            f_read = f.read()
            self.f_split = f_read.split("\n")
    
            for i in self.f_split:
                if i != '':
                    self.id_list.append(i.split("#")[0])
                    self.salary_list.append(i.split("#")[3])
        self.display()
    
    def sorting(self):
        
        for i in self.f_split:
            if i != '':
                if i.split("#")[1] not in self.name_list:
                    self.name_list.append(i.split("#")[1])
        
        self.name_list.sort()
        
        self.new_list = []
        for i in self.name_list:
            
            for j in self.f_split:
                
                if j[6:6+len(i)] == i:
                    self.new_list.append(j)
        
        for i in self.new_list:
            if i.split("#")[0] not in self.id_list:
                self.id_list.append(i.split("#")[0])
                    

    def new_staff(self):
        print("New Staff")
        
        while True:
            ID = input("Input ID[SXXXX]:").upper()
            if ID[0] != "S":
                print("ID must start with an S")

            elif len(ID) != 5:
                print("ID must be 5 characters long")
            
            try:
                int(ID[1:])
            except ValueError:
                print("Last 4 characters of ID must be integers")
                continue

            if ID in self.id_list:
                print("ID already exists")

            else:
                break
        
        while True:
            name = input("Input Name[0...20]:").title()
            if len(name) > 20:
                print("Name should not be over 20 characters long")
            else:
                break
        
        while True:
            position = input("Input Position[Staff|Officer|Manager]:").title()
            if position not in ["Staff",'Officer','Manager']:
                print("Please enter a valid position")
            else:
                break

        while True:
            salary = input("Input salary for {}:".format(position))
            try:
                int(salary)
            except ValueError:
                print("Please enter in integers")
                continue

            if position == "Staff" and int(salary) not in range(3500000,7000000):
                print("Salary not in range")

            elif position == "Officer" and int(salary) not in range(7000001,10000000):
                print("Salary not in range")
                
            elif position == 'Manager' and int(salary) < 10000001:
                print("Salary not in range")
                
            else:
                break
        
        self.f_split.append("{}#{}#{}#{}".format(ID,name,position,salary))
        self.display()
        

    def delete_staff(self):
        self.sorting()
        print("Delete Staff")
        ID_del = input("Input ID[SXXXX]:").upper()
        if ID_del not in self.id_list:
            print("Data not found")
            self.display()
        else:
            tempdata1 = []
            for i in self.f_split:
                tempdata1.append(i.split("#")[0])
            
            tempdata2 = tempdata1.index(ID_del)
            
            del self.f_split[tempdata2]
            tempdata3 = self.id_list.index(ID_del)
            del self.new_list[tempdata3]
            print("Data has been successfully deleted")
            self.display()
        
    def view(self):
        for i in self.f_split:
            if i != '':
                if i.split("#")[2] == "Staff":
                    self.staff_salary.append(int(i.split("#")[3]))
                elif i.split("#")[2] == "Officer":
                    self.officer_salary.append(int(i.split("#")[3]))
                elif i.split("#")[2] == "Manager":
                    self.manager_salary.append(int(i.split("#")[3]))
        
        print("1. Staff\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}\n".format(min(self.staff_salary),max(self.staff_salary),mean(self.staff_salary)))
        print("2. Officer\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}\n".format(min(self.officer_salary),max(self.officer_salary),mean(self.officer_salary)))
        print("3. Manager\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}\n".format(min(self.manager_salary),max(self.manager_salary),mean(self.manager_salary)))
        self.display()

    def save(self):
        with open('test.txt','w') as f:
            for i in self.new_list:
                f.write(i+"\n")
        
    def display(self):
        print("|ID{}|Name{}|Position{}|Salary{}|".format(" "*(8-2)," "*(20-4)," "*(20-8)," "*(len(str(max(self.salary_list)))+2-6)))
        self.sorting()
        for i in self.new_list:
            print("|{}|{}|{}|{}|".format(i.split("#")[0]+" "*(8-len(i.split("#")[0])),i.split("#")[1]+" "*(20-len(i.split("#")[1])),i.split("#")[2]+" "*(20-len(i.split("#")[2])),i.split("#")[3]+" "*(len(str(max(self.salary_list)))+2-len(i.split("#")[3]))))
        print("\n\n")
        print("1. New Staff")
        print("2. Delete Staff")
        print("3. View Summary Data")
        print("4. Save & Exit")
        while True:
           action = input("Input Choice:")
           if action in "1234":
               break
        if action == '1':
            self.new_staff()
        
        if action == '2':
            self.delete_staff()
        
        if action == '3':
            self.view()

        if action == '4':
            self.save()
        
Employee()
