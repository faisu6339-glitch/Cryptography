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
    return filename
file=input("Enter the filename (without extension): ")
write_textfile(file)
