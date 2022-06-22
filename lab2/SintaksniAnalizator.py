import sys

revert = ""
check = bool(len(revert) == 0)
text = ""
helpText = ""
tab = 1
num = 0
list = ["IDN", "KR_ZA"]
list1 = ["KR_AZ", "⏊"]
list2 = ["IDN", "KR_ZA", "⏊"]
list3 = ["IDN", "BROJ", "OP_PLUS", "OP_MINUS", "L_ZAGRADA"]
list4 = ["IDN","BROJ","OP_PLUS","OP_MINUS","L_ZAGRADA"]
T_list = ["IDN","KR_ZA","KR_DO","KR_AZ","OP_PLUS","OP_MINUS","D_ZAGRADA","⏊"]
E_list = ["IDN","KR_ZA","KR_DO","KR_AZ","D_ZAGRADA","⏊"]

def errMsg(file, num):
    print("err", file[num][0] + " " + file[num][1] + " " + file[num][2])

def getItem(file, posX, posY):
    return file[posX][posY]

def addName(input):
    global text
    text = text + input

def addChild(file):
    global text
    global num
    text = text + file[num][0] + " " + file[num][1] + " " + file[num][2]

def loop(file, tab):
    global text
    global revert
    global num
    for i in range(tab):
        text = text + " "
    addName("<za_petlja>\n")
    num1 = num
    tmp_item = getItem(file,num1,0)
    if (tmp_item == "KR_ZA"):
        if (bool(len(revert) == 0)):
            for i in range(tab+1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
            tmp_item = getItem(file,num1+1, 0)
            if (tmp_item == "IDN"):
                for i in range(tab+1):
                    text = text + " "
                addChild(file)
                text = text + "\n"
                num = num + 1
            else:
                errMsg(file,num)
                quit()
            tmp_item = getItem(file, num1+2, 0)
            if (tmp_item == "KR_OD"):
                for i in range(tab+1):
                    text = text + " "
                addChild(file)
                text = text + "\n"
                num = num + 1
            else:
                errMsg(file,num)
                quit()
            if (file[num1 + 3][0] in list4):
                E(file, tab + 1)
            else:
                errMsg(file,num)
                quit()
            for i in range(tab+1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
            E(file, tab + 1)
            functions(file, tab + 1)
            for i in range(tab+1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
        else:
            print("err kraj")
            quit()
    else:
        errMsg(file,num)
        quit()

def start(file):
    global text
    global num
    global helpText
    if (fileLength != 0):
        tmp = file[num][0]
        if (tmp in list2):
            addName("<program>\n")
            functions(file, tab)
        else:
            errMsg(file,num)
            helpText[0] = ""
    else:
        helpText = ""
        quit()

def functions(file, tab):
    global text
    global num
    global helpText
    num1 = num
    for i in range(0,tab):
        text = text + " "
        helpText = helpText + " "
    addName("<lista_naredbi>\n")
    if (num1 <= fileLength-1):
        helpText = helpText + "<lista_naredbi>\n"
        if(file[num1][0] in list1):
            tab = tab + 1
            num2 = tab
            for i in range(num2):
                helpText = helpText + " "
            for i in range(0, tab):
                text = text + " "
            addName("$\n")
            num3 = num2 + 1
            if (num3 < tab):
                helpText = text
            else:
                helpText = ""
        elif (file[num1][0] in list):
            tab = tab + 1
            function(file, tab)
            functions(file, tab)
    else:
        tab = tab + 1
        for i in range(0, tab):
            text = text + " "
        addName("$\n")

def function(file, tab):
    global text
    global num
    num1 = num
    cond = bool(num1 <= fileLength - 1)
    for i in range(0, tab):
        text = text + " "
    addName("<naredba>\n")
    if(cond):
        tmp_item = getItem(file, num, 0)
        if (tmp_item == "KR_ZA"):
            loop(file, tab + 1)
        elif(tmp_item == "IDN"):
            addFunction(file, tab+1)
        else:
            errMsg(file,num)
            quit()
    else:
        print("err kraj")
        quit()

def addFunction(file, tab):
    global text
    global num
    num1 = num
    for i in range(0, tab):
        text = text + " "
    addName("<naredba_pridruzivanja>\n")
    tmp_item = getItem(file, num1, 0)
    if (tmp_item == "IDN"):
        for i in range(tab+1):
            text = text + " "
        addChild(file)
        text = text + "\n"
        num = num + 1
        tmp_item = getItem(file, num1+1,0)
        if(tmp_item == "OP_PRIDRUZI"):
            for i in range(tab+1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
            E(file, tab+1)
        else:
            errMsg(file,num)
            quit()
    else:
        errMsg(file,num)
        quit()

def E_lista(file, tab):
    global text
    global num
    for i in range(tab):
        text = text + " "
    addName("<E_lista>\n")
    num1 = num
    if (num <= fileLength - 1):
        tmp_item = getItem(file, num1, 0)
        if (tmp_item == "OP_PLUS"):
            for i in range(tab + 1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
            E(file, tab + 1)
        elif (tmp_item == "OP_MINUS"):
            for i in range(tab + 1):
                text = text + " "
            addChild(file)
            text = text + "\n"
            num = num + 1
            E(file, tab + 1)
        elif (tmp_item in E_list):
            for i in range(tab + 1):
                text = text + " "
            addName("$\n")
    else:
        for i in range(tab+1):
            text = text + " "
        addName("$\n")

def opPuta(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1
    T(file, tab + 1)

def opDijeli(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1
    T(file, tab + 1)

def opPlus(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1
    P(file, tab + 1)

def opMinus(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    text = text + file[num][0] + " " + file[num][1] + " " + file[num][2]
    text = text + "\n"
    num = num + 1
    P(file, tab + 1)

def broj(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1

def idn(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1

def zagrada(tab):
    global num
    global text
    for i in range(tab + 1):
        text = text + " "
    addChild(file)
    text = text + "\n"
    num = num + 1
    E(file, tab + 1)

def T_lista(file, tab):
    global text
    global num
    for i in range(tab):
        text = text + " "
    addName("<T_lista>\n")
    num1 = num
    if(num <= fileLength-1):
        tmp_item = getItem(file,num1,0)
        if(tmp_item == "OP_PUTA"):
            opPuta(tab)
        elif(tmp_item == "OP_DIJELI"):
            opDijeli(tab)
        elif(tmp_item in T_list):
            for i in range(tab+1):
                text = text + " "
            addName("$\n")
        else:
            errMsg(file,num)
            quit()
    else:
        for i in range(tab+1):
            text = text + " "
        addName("$\n")

def E(file, tab):
    global text
    global num
    num1 = num
    for i in range(tab):
        text = text + " "
    addName("<E>\n")
    if(num <= (fileLength-1)):
        if(file[num1][0] in list3):
            T(file, tab+1)
            E_lista(file, tab+1)
        else:
            errMsg(file,num)
            quit()
    else:
        print("err kraj")
        quit()

def T(file, tab):
    global text
    for i in range(tab):
        text = text + " "
    addName("<T>\n")
    if(file[num][0] in list3):
        P(file, tab+1)
        T_lista(file, tab+1)
    else:
        errMsg(file,num)
        quit()

def P(file, tab):
    global revert
    global text
    global num
    num1 = num
    for i in range(tab):
        text = text + " "
    addName("<P>\n")
    tmp_item = getItem(file, num1, 0)
    if (tmp_item == "OP_PLUS"):
        opPlus(tab)
    elif (tmp_item == "OP_MINUS"):
        opMinus(tab)
    elif (tmp_item == "L_ZAGRADA"):
        zagrada(tab)
        for i in range(tab+1):
            text = text + " "
        cnt = num
        if (cnt < len(file)):
            tmp1_item = getItem(file,cnt,0)
            if (tmp1_item != "D_ZAGRADA" and bool(len(revert) == 0)):
                errMsg(file,num)
                quit()
            else:
                addChild(file)
                text = text + "\n"
                num = num + 1
        else:
            print("err kraj")
            quit()
    elif (tmp_item == "IDN"):
        idn(tab)
    elif (tmp_item == "BROJ"):
        broj(tab)
    else:
        errMsg(file,num)
        quit()

file = sys.stdin.readlines()
fileLength = len(file)
for i in range(fileLength):
    file[i] = file[i].rstrip().rsplit()

start(file)
if(bool(len(revert) != 0)):
    print(revert,end="")
else:
    print(text,end="")