# Подсчитать количество букв «а» во введенной строке

# TODO: your code here
text = input("Text: ")

i=0
c=0
while i<len(text):
    if text[i] == "a":
        c+=1
    i+=1

print(c, "симвлов в строке")
