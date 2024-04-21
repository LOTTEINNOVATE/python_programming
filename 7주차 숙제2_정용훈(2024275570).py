from google.colab import drive
drive.mount('/content/gdrive')

with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'w') as writefile:
    writefile.write("This is line A")

with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('/content/gdrive/My Drive/Colab Notebooks/example10.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    writefile.write("This is line 10\n")

with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")

with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

Lines = ['This is line A\n', 'This is line B\n','This is line C\n']
Lines
print(Lines)

with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")

with open('/content/gdrive/My Drive/Colab Notebooks/example3.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt','r')as readfile:
    whit open('/content/gdrive/My Drive/Colab Notebooks/example12.txt', 'w') as writefile:
    for line in readfile:
        writefile.write(line)

with open('/content/gdrive/My Drive/Colab Notebooks/example12.txt','r') as testwritefile:
    print(testwritefile.read())

with open('/content/gdrive/My Drive/Colab Notebooks/example12.txt', 'r') as testwritefile:
    print(testwritefile.read())