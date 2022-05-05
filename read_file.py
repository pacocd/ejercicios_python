from pickle import load

def readFile(name, mode):
    with open(name, mode) as file:
        print(file)
        return load(file)


fileContent = readFile("list.bin", "rb")

print(fileContent)
print(type(fileContent))
