import module1 as m

while True:
    print("1. Write to a file")
    print("2. Read from a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        filename=input("Enter the filename (without extension): ")
        m.write_textfile(filename)
    elif choice == '2':
        filename=input("Enter the filename (without extension): ")
        
        r=m.read_textfile(filename)
        print(r)

    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
