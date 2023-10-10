file = open("dictionary.txt", "r")
data = file.read()

list = data.replace('\n', ", ").split(".")


print(list)
file.close()