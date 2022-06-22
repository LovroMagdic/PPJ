import sys

def mynewparser(ea):

    parsed1 = []
    for char in ea:
        parsed1.append(char)

    dummy_str = ""
    temp = []
    for each in parsed1:
        if each.isalpha() or each.isnumeric():
            dummy_str = dummy_str + each
        if each in operator:
            temp.append(dummy_str)
            dummy_str = ''
            temp.append(each)
    temp.append(dummy_str)
    for each in temp:
        myparser(each)

def myparser(ea):
    if ea.isalpha() and ea != "za" and ea != "az" and ea != "od" and ea != "do":
        print('{} {} {}'.format("IDN", count, ea))

    elif ea.isnumeric():
        print('{} {} {}'.format("BROJ", count, ea))

    elif ea == "=":
        print('{} {} {}'.format("OP_PRIDRUZI", count, ea))

    elif ea == "+":
        print('{} {} {}'.format("OP_PLUS", count, ea))

    elif ea == "-":
        print('{} {} {}'.format("OP_MINUS", count, ea))

    elif ea == "*":
        print('{} {} {}'.format("OP_PUTA", count, ea))

    elif ea == "/":
        print('{} {} {}'.format("OP_DIJELI", count, ea))

    elif ea == "(":
        print('{} {} {}'.format("L_ZAGRADA", count, ea))

    elif ea == ")":
        print('{} {} {}'.format("D_ZAGRADA", count, ea))

    elif ea == "za":
        print('{} {} {}'.format("KR_ZA", count, ea))

    elif ea == "az":
        print('{} {} {}'.format("KR_AZ", count, ea))

    elif ea == "od":
        print('{} {} {}'.format("KR_OD", count, ea))

    elif ea == "do":
        print('{} {} {}'.format("KR_DO", count, ea))


amIHere = "=()+-"
op = ["+", "-", "*", "/"]
operator = "*+-/()"

Lines = sys.stdin.readlines()
#f = open("test.in", "r")
#Lines = f.readlines()

list = []

for line in Lines:
    head, sep, tail = line.partition('//')
    list.append(head)

count = 0
tmp = ''
parsed = ''
for each in list:
    if each == '':
        count += 1
    elif each != '':
        count += 1
        tmp = each
        if "\n" in tmp:
            tmp = tmp.replace("\n", " ")
        parsed = tmp.split(" ")
        for ea in parsed:
            if ea != " " and not (ea.isalpha()) and not (ea.isnumeric()) and not (ea in amIHere):
                mynewparser(ea)
            myparser(ea)

#jesam te prebacio