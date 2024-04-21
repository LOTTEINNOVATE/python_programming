from drive.google.com import drive
drive.mount('/content/gdrive')

example1 = "/content/gdrive/My_Drive/Colab Notebooks/example1.txt"
file1 = open(example1, "r")

file1.name
print(file1.name)

file1.mode
print(file1.mode)

FileContent = file1. read()
FileContent
print(FileContent)

type(FileContent)

file1.close()

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

file1.close()
print(file1.close())

file1.closed
print(file1.closed)

print(FileContent)

with open(example1, "r") as file1:
    print(file1.read(4))

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    print("second line: " +file1.readline())
    print("third line: " +file1.readline())

with open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("lteration", str(i), "i ", line)
        i = i + 1;

    with open(example1, "r") as file1:
        FileasList = file1. readlines()

    FileasList[0]

    FileasList[1]

    FileasList[2]

    FileasList[3]

    FileasList[4]


