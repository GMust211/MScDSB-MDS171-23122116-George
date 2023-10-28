class student:
    def _init_(self):
        self.details={}
    def det(self,name,reg_no,sub1,sub2,sub3,sub4):
        total_marks=sub1+sub2+sub3+sub4
        self.stu={
            "Name" : name,
            "Reg No" : reg_no,
            "SUB 1" : sub1,
            "SUB 2" : sub2,
            "SUB 3" : sub3,
            "SUB 4" : sub4,
            "Total Marks" : total_marks
        } 
        self.stu[reg_no]=self.det
        print(self.stu)
        #return reg_no
    def search(self,Reg):
        for key in self.stu.keys():
            flag=True
            if Reg==key:
                print(self.stu[key])
                exit()
            else:
                flag== "False"
        if flag=="False":
            print("Student not found")
obj=student()
while True:
    print("MENU OPTIONS")
    print("*"*30)
    print("1.Teacher Login")
    print("2.Student Login")
    print("3.Exit")
    choice=input(("Enter your Choice"))
    if choice=="1":
        while True:
            print("1.Update Marks")
            print("2.Search Student")
            print("3.Exit")
            choice1=input("Enter your new choice")
            if choice=="1":
                name=input("Enter your name")
                reg_no=int(input("Enter your Register NO."))
                sub1=int(input("Enter Subject 1 Marks"))
                sub2=int(input("Enter Subject 2 Marks"))
                sub3=int(input("Enter Subject 3 Marks"))
                sub4=int(input("Enter Subject 4 Marks"))
                obj.det(name,reg_no,sub1,sub2,sub3,sub4)            
            elif choice=="2":
                Reg=input("Enter the name to be searched :")
                obj.search(Reg)
            elif choice=="3":
                exit() 
    if choice=="2":
        Reg=input("Enter the Name to be searched :")
        obj.search(Reg)
    if choice=="3":
        exit()
    break