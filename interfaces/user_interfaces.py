def create_user(user_data):
    name = input("Enter user name: ")
    user_data.append({"name": name})
    print(f"User '{name}' created successfully.")


def start(user_data):

    print("===================================")
    print("           Foundry AI")
    print("===================================")
    while True:
        print("\nMain Menu:")
        print("1.Create User")
        print("2.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You have selected to create a user.")
            create_user(user_data)
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")