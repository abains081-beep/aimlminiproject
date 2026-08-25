library = [
    [101, "Python", "John Doe", "Available"],
    [102, "Data Structures", "Jane Smith", "Not Available"],
    [103, "Algorithm Design", "Alan Turing", "Borrowed"],
    [104, "AI&ML", "Sumanyu Singh", "Available"]
]

print("--> WELCOME TO THE LIBRARY MANAGEMENT SYSTEM <--")

while True:
    print("\n--- Main Menu ---")
    print("1. View All Books\n2. Add a New Book\n3. Borrow a Book\n4. Return a Book\n5. Search for a Book\n6. Exit \n7.Gift")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n--- Library Catalog ---")
        print("ID\t| Title\t\t\t| Author\t\t| Status")
        print("-" * 65)
        for book in library:
            print(f"{book[0]}\t| {book[1]:<20} | {book[2]:<18} | {book[3]} | {book[4]}")

    elif choice == "2":
        book_id = int(input("Enter unique Book ID: "))
        if any(book[0] == book_id for book in library):
            print("Error: A book with this ID already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.append([book_id, title, author, "Available"])
            print(f"Success: '{title}' added.")

    elif choice == "3" or choice == "4":
        action = "borrow" if choice == "3" else "return"
        target_id = int(input(f"Enter Book ID you want to {action}: "))
        
        found = False
        for book in library:
            if book[0] == target_id:
                found = True
                if choice == "3" and book[3] == "Available":
                    book[3] = "Borrowed"
                    print(f"Success: Borrowed '{book[1]}'.")
                elif choice == "4" and book[3] == "Borrowed":
                    book[3] = "Available"
                    print(f"Success: Returned '{book[1]}'.")
                else:
                    print(f"Error: Cannot {action} this book (Status: {book[3]}).")
                break
        if not found:
            print("Error: Book ID not found.")

    elif choice == "5":
        query = input("Enter Title or Author to search: ").lower()
        print("\nID\t| Title\t\t\t| Author\t\t| Status")
        print("-" * 65)
        match = False
        for book in library:
            if query in book[1].lower() or query in book[2].lower():
                print(f"{book[0]}\t| {book[1]:<20} | {book[2]:<18} | {book[3]}")
                match = True
        if not match:
            print("No matching books found.")

    elif choice == "6":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid option! Enter 1-6.")
    if choice =="0":
        print("please select a velid number")
        break
    library = [
    [101, "Python", "John Doe", "Available"],
    [102, "Data Structures", "Jane Smith", "Not Available"],
    [103, "Algorithm Design", "Alan Turing", "Borrowed"],
    [104, "AI&ML", "Sumanyu Singh", "Available"]
]

print("--> WELCOME TO THE LIBRARY MANAGEMENT SYSTEM <--")

while True:
    print("\n--- Main Menu ---")
    print("1. View All Books\n2. Add a New Book\n3. Borrow a Book\n4. Return a Book\n5. Search for a Book\n6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n--- Library Catalog ---")
        print("ID\t| Title\t\t\t| Author\t\t| Status")
        print("-" * 65)
        for book in library:
            print(f"{book[0]}\t| {book[1]:<20} | {book[2]:<18} | {book[3]}")

    elif choice == "2":
        book_id = int(input("Enter unique Book ID: "))
        if any(book[0] == book_id for book in library):
            print("Error: A book with this ID already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.append([book_id, title, author, "Available"])
            print(f"Success: '{title}' added.")

    elif choice == "3" or choice == "4":
        action = "borrow" if choice == "3" else "return"
        target_id = int(input(f"Enter Book ID you want to {action}: "))
        
        found = False
        for book in library:
            if book[0] == target_id:
                found = True
                if choice == "3" and book[3] == "Available":
                    book[3] = "Borrowed"
                    print(f"Success: Borrowed '{book[1]}'.")
                elif choice == "4" and book[3] == "Borrowed":
                    book[3] = "Available"
                    print(f"Success: Returned '{book[1]}'.")
                else:
                    print(f"Error: Cannot {action} this book (Status: {book[3]}).")
                break
        if not found:
            print("Error: Book ID not found.")

    elif choice == "5":
        query = input("Enter Title or Author to search: ").lower()
        print("\nID\t| Title\t\t\t| Author\t\t| Status")
        print("-" * 65)
        match = False
        for book in library:
            if query in book[1].lower() or query in book[2].lower():
                print(f"{book[0]}\t| {book[1]:<20} | {book[2]:<18} | {book[3]}")
                match = True
        if not match:
            print("No matching books found.")

    elif choice == "6":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid option! Enter 1-6.")
    if choice =="0":
        print("please select a velid number")
        break
    else:
        print("Thankyou for visiting")
      
