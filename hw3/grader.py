with open("hw3.py", 'r+') as f:
    if f.readline().strip() != "from nodes import *":
        f.seek(0,0)
        content = f.read()
        f.seek(0, 0)
        f.write("from nodes import *".rstrip('\r\n') + '\n' + content)

from hw3 import *
from nodes import *
import logging

def main():
    if prob1() == 0:
        print("****************************************************************#1 Kleinfeldt [PASSED]\n")
    else:
        print("*****************************************************************#1 Kleinfeldt [ERROR]\n")
    if prob2() == 0:
        print("********************************************************************#2 Ladder [PASSED]\n")
    else:
        print("*********************************************************************#2 Ladder [ERROR]\n")
    if prob3() == 0:
        print("***************************************************************#3 findLargest [PASSED]\n")
    else:
        print("****************************************************************#3 findLargest [ERROR]\n")
    if prob4() == 0:
        print("**********************************************************#4 Majority Element [PASSED]\n")
    else:
        print("***********************************************************#4 Majority Element [ERROR]\n")
    if prob5() == 0:
        print("*****************************************************************#5 findValue [PASSED]\n")
    else:
        print("******************************************************************#5 findValue [ERROR]\n")
    if prob6() == 0:
        print("*************************************************************#6 findLastValue [PASSED]\n")
    else:
        print("**************************************************************#6 findLastValue [ERROR]\n")

def prob1():
    flag = 0
    try:
        if kleinfeldt(1) != 1:
            print(kleinfeldt(1))
            flag += 1
        if kleinfeldt(2) != 1.25:
            print(kleinfeldt(2))
            flag += 1
        if round(kleinfeldt(5), 7) != 1.4636111:
            print(kleinfeldt(5))
            flag += 1
        if round(kleinfeldt(100),7) != 1.6349839:
            print(kleinfeldt(100))
            flag += 1
        return flag
    except:
        return crash(flag)

def prob2():
    flag = 0
    try:
        if ladder(1) != 1:
            flag += 1
        if ladder(2) != 2:
            flag += 1
        if ladder(3) != 3:
            flag += 1
        if ladder(4) != 5:
            flag += 1
        if ladder(5) != 8:
            flag += 1
        if ladder(13) != 377:
            flag += 1
        return flag
    except:
        return crash(flag)

def prob3():
    flag = 0
    a = [6,8,2,34,6,7,94,234,2,89,67,2,34]
    try:
        if findLargest(a) != 234:
            print("Was expecting 234 but got ", findLargest(a))
            flag += 1
        return flag
    except:
        return crash(flag)

def prob4():
    flag = 0
    a1 = [1,4,1,4]
    a2 = [1,4,1,4,1]
    a3 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5]
    a4 = [2,7,2,7,2,7,2,7,2,7,2,7,2,7]
    a5 = [1,2,1,3,1,9,1,1,1,4,5,1,1,6,6,7,7,1,1]

    try:
        b1 = findPossibilities(a1)
        b2 = findPossibilities(a2)
        b3 = findPossibilities(a3)
        b4 = findPossibilities(a4)
        b5 = findPossibilities(a5)

        if b1 != []:
            print("FIND ERROR")
            print("Was expecting [] but got ", b1)
            flag += 1
        if b2 != [1]:
            print("FIND ERROR")
            print("Was expecting [1] but got ", b2)
            flag += 1
        if b3 != [3,5] and b3 != [3,3]:
            print("FIND ERROR")
            print("Was expecting [3,5] or [3,3] but got ", b3)
            flag += 1
        if b4 != []:
            print("FIND ERROR")
            print("Was expecting [] but got ", b4)
            flag += 1
        if b5 != [1,1]:
            print("FIND ERROR")
            print("Was expecting [1,1] but got ", b5)
            flag += 1
    except:
        logging.exception("_____crashed!")
        flag += 1

    try:
        c1 = verifyPossibilities(a1, [])
        c2 = verifyPossibilities(a2, [1])
        c3 = verifyPossibilities(a3,[3,5])
        c4 = verifyPossibilities(a4, [])
        c5 = verifyPossibilities(a5, [1,1])

        if c1 != None:
            print("VERIFY ERROR")
            print("Was expecting None but got ", c1)
            flag += 1
        if c2 != 1:
            print("VERIFY ERROR")
            print("Was expecting 1 but got ", c2)
            flag += 1
        if c3 != 3:
            print("VERIFY ERROR")
            print("Was expecting 3 but got ", c3)
            flag += 1
        if c4 != None:
            print("VERIFY ERROR")
            print("Was expecting None but got ", c4)
            flag += 1
        if c5 != 1:
            print("VERIFY ERROR")
            print("Was expecting 1 but got ", c5)
            flag += 1

        return flag

    except:
        return crash(flag)

def prob5():
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n3.setNext(n4)
    n2.setNext(n3)
    n1.setNext(n2)

    flag = 0

    try:
        if findValue('A', n1) != True:
            print("Was expecting True but got ", findValue('A', n1))
            flag +=1
        if findValue('D', n1) != True:
            print("Was expecting True but got ", findValue('D', n1))
            flag +=1
        if findValue(9, n1) != False:
            print("Was expecting False but got ", findValue(9, n1))
            flag +=1
        return flag
    except:
        return crash(flag)    

def prob6():
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n3.setNext(n4)
    n2.setNext(n3)
    n1.setNext(n2)

    flag = 0

    try:
        if findLastValue(n1) != 'D':
            print("Was expecting 'D' but got ", findLastValue(n1))
            flag += 1
        return flag
    except:
        return crash(flag)

def crash(flag):
    logging.exception("_____crashed!")
    flag += 1
    return flag

if __name__ == "__main__":
    main()