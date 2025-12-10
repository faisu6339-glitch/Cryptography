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