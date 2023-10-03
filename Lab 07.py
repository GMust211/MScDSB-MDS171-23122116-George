# class MSCDSB:
#     def __init__(self):
#         self.name="MSC DS B"
#         #datamembers /properties/attributes
#         self.students=["A","B","c"]
#     def printstudents(self):
#         for student in self.students:
#             print(student)
# obj = MSCDSB()
# print(obj.name, obj.students)
# obj.printstudents()

# class car:
#     def __init__(self,mfg,mdl,yer):
#         self.manufacture=mfg
#         self.model=mdl
#         self.year=yer
# bmw = car("BMW","F-Series",2020)
# print(bmw.manufacture,bmw.model,bmw.year)
# ferrari = car("Ferrari","Mista Rossa",2021)
# print(ferrari.manufacture,ferrari.model,ferrari.year)
# manufacture=input("Enter Manufacture :")
# model=input("Enter the model : ")
# year=input("Enter the year : ")
# audi = car(manufacture,model,year)
# print(audi.manufacture,audi.model,audi.year)

# create a class restaurent that accepts 
# itemname nad quantity as input
# inside your class ypou are having the item
# abd its costs (unit price) as a dictionary
# create a funtion and calculate totalcost
# that prints the itemname, qty & totalcost

# class resturant:
#     def __init__(self,itemname,qty):
#         self.itemname = itemname
#         self.qty = qty
#         self.menuitems={
#             "RICE" : 30,
#             "CHICKEN" : 100,
#             "DAL" : 40,
#             "CHAPATHI" : 15
#         }
#     def totalCost(self):
#         print("Enter the cost of the order : ")
#         print("Item\t:",self.itemname)
#         print("Quantity\t:",self.qty)
#         total = self.qty * self.menuitems[self.itemname]
#         print("Total\t",total)
# order = resturant("RICE",4)
# order.totalCost()

# class resturant:
#     def __init__(self,itemname,qty):
#         self.itemname = itemname
#         self.qty = qty
#         self.menuitems={
#             "RICE" : 30,
#             "CHICKEN" : 100,
#             "DAL" : 40,
#             "CHAPATHI" : 15
#         }
#     def totalCost(self):
#         print("Item\t:",self.itemname)
#         print("Quantity\t:",self.qty)
#         total = self.qty * self.menuitems[self.itemname]
#         print("Total\t",total)
# itemname = input("Item Name ? : ")
# qty = int(input("Quantity ? : "))
# order = resturant(itemname,qty)
# order.totalCost()

# define a class expenses tracker that stores the 
# expenditure and income is a dictionary
# impliment the method to:
# -store the transaction
# -view transaction
# -calaulate the total expense/income

class expenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

    def store_to_csv(self):
        with open("examplefile.csv" , "w+") as file:
            for item in self.expenseDict['income']:
                file.write(str(item))

# define a menu that will let users to enter expense, view expenses
# or income, get totals in each and exit from the program


def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details




myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Store the details to a csv file.")
    print("6. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        myexpense.store_to_csv()
    elif choice == 6:
        exit()
    else:
        print("In valid choice")


# HOME WORK
# create a method in  the class
# to export the detaoils in the form of csv
# add export details to a file in the menu option