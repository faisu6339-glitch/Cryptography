def write_textfile(filename):
    filename += ".txt"
    file= open(filename, "w")
    while True:
        text = input("Enter text to write to the file (or type 'exit' to finish): ")
        if text.lower() == 'exit':
            break
        file.write(text + "\n")
    file.close()
    print("File written successfully.")

def read_textfile(filename):
    filename += ".txt"
    file= open(filename, "r")
    if file:
        content = file.read()
        file.close()
        print("File content:")
        print(content)
    else:
        print("File not found.")
    return content