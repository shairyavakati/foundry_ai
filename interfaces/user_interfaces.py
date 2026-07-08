def start():

    print("Welcome to FOUNDRY_AI")
    while True:
        print("\nMain Menu:")
        print("1.Name:")
        print("2.Mobile Number:")
        print("3.E-mail:")
        print("4.Exit")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            name = input("Enter Name: ")

        elif choice == "2":
            mobile =input("Enter Mobile Number: ")  
        elif choice == "3":
            email =input("Enter E-mail: ")
        else:
            print("Exiting the program.")
            break