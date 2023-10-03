class Stack:
    
    def __init__ (self):
        self.items=[]

    def push(self,item):
        self.items.append(value)
        print(value)
    def pop(self):
        popitem = self.items.pop()
        print("Popped :"+ popitem)

    def search(self,name):
        
        if name in self.items:
            print("name "+name+" is present")
        else:
            print("Name you are searching is not here!!")
    def printstack(self):
        print(self.items)
    def topitem(self):
        print("The Peek value is : ",(self.items[-1]))
    def emptystack(self):
        if len(self.items)==0:
            print("The Stack is Empty!!")
        else:
            print("The Stack is not Empty!!")

stack = Stack()
while True:
        print("Menu Options")
        print("*"*30)
        print("1. Push into stack  ")
        print("2. Pop a name  ")
        print("3. Search a name  ")
        print("4. List all names  ")
        print("5. Show the top item  ")
        print("6. Check whether stack is empty  ")
        print("7. Exit")

        choice = int(input("Enter your Choice : "))

        if choice == 1:
            value = input("Enter the name to be added: ")
            stack.push(value)

        elif choice == 2:
            
            stack.pop()
        elif choice == 3:
            name= input("Enter the name to be searched: ")
            stack.search(name)
        elif choice == 4:
            stack.printstack()
        elif choice == 5:
            stack.topitem()
        elif choice == 6:
            stack.emptystack()
        elif choice == 7:
            exit()
        else:
            print("Invalid Choice!!!")
