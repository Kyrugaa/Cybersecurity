file = open("dictionary.txt", "r")
data = file.read()

#list = data.replace('\n', ", ").split(".")
list = data.split('\n')

print(list)
file.close()
