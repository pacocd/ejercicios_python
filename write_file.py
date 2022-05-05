from pickle import dump, load
from read_file import readFile

def writeFile(name, mode, content):
    with open(name, mode) as file:
        dump(content, file)

writeFile("write.py", "wb", ["test", "1"])
print("done")
print(readFile("write.py", "rb"))
