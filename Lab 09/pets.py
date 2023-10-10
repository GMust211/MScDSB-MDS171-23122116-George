import petstore

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Store a New Pet")
        print("2. List All Pets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter pet's name: ")
            species = input("Enter pet's species: ")
            age = input("Enter pet's age: ")
            price = input("Enter pet's price: ")
            petstore.store_pet(name, species, age, price)
        elif choice == "2":
            petstore.list_pets()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Search for a Pet")
        print("2. List All Pets")
        print("3. Buy a Pet")
        print("4. Exit")
def menu():
    while True:
        print("\nUser Menu:")
        print("1. Search for a Pet")
        print("2. List All Pets")
        print("3. Buy a Pet")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter pet's name to search: ")
            pet_info = petstore.search_pet(name)
            if pet_info:
                print(f"Pet found - ID: {pet_info[0]}, Name: {pet_info[1]['name']}, Species: {pet_info[1]['species']}, Age: {pet_info[1]['age']}, Price: ${pet_info[1]['price']}")
            else:
                print("Pet not found in inventory.")
        elif choice == "2":
            petstore.list_pets()
        elif choice == "3":
            pet_id = input("Enter the ID of the pet you want to buy: ")
            petstore.sell_pet(int(pet_id))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        print("\nWelcome to the PetStore")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role_choice = input("Enter your role: ")

        if role_choice == "1":
            admin_menu()
        elif role_choice == "2":
            user_menu()
        elif role_choice == "3":
            break
        else:
            print("Invalid role choice. Please try again.")
