# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
s=0
not_space_symb = 0
with open("data/limericks.txt","r",encoding="utf-8") as f:
    for line in f:
        for el in line:
            if el not in (" ", "\n","\t"):
                not_space_symb+=1
        if line == "\n": s+=1
        print(line.rstrip())
print("\nnot_space_symb: ",not_space_symb)
print("s: ",s+1)
