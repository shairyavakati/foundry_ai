from scripts.fetch_users import view_users
from scripts.add_user import add_user
from scripts.update_user import update_user
from scripts.delete_user import delete_user

print("===================================")
print("      Welcome to Foundry AI")
print("===================================")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. View Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_users()

    elif choice == "2":
        add_user()

    elif choice == "3":
        update_user()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        print("Thank you for using Foundry AI!")
        break

    else:
        print("Invalid choice! Please try again.")