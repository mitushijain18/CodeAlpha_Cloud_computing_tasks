database = []

def add_data(data):
    if data not in database:
        database.append(data)
        print("Unique data added successfully.")
    else:
        print("Duplicate data found. Entry rejected.")

while True:
    print("\n1. Add Data")
    print("2. View Database")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        data = input("Enter data: ")
        add_data(data)

    elif choice == "2":
        print("\nDatabase Records:")
        for item in database:
            print(item)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
        print("Invalid choice.")