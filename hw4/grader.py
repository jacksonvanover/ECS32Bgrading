def insertHashTableClass():
    f1 = open("hw4.py", 'r+')
    f1.seek(0,0)
    studentCode = f1.readlines()
    f1.seek(0,0)

    f2 = open("hashTableIncomplete.py", 'r')
    f2.seek(0,0)
    hashTableClass = f2.readlines()
    f2.close()

    i = 0
    j = 0
    flag = False
    while "def put(" not in studentCode[i] and i < len(studentCode):
        if "class Hash" in studentCode[i] or "class hash" in studentCode[i]:
            i += 1
            flag = True
            while "def put(" not in studentCode[i] and i < len(studentCode):
                i += 1
            break
        else:
            f1.write(studentCode[i])
            i += 1
    while "# insert put method here" not in hashTableClass[j] and j < len(hashTableClass):
        f1.write(hashTableClass[j])
        j += 1
    while i < len(studentCode):
        if "def hash" in studentCode[i]:
            break
        elif flag:
            f1.write(studentCode[i])
        else:
            f1.write("    " + studentCode[i])
        i += 1
    j += 1
    while j < len(hashTableClass):
        f1.write(hashTableClass[j])
        j += 1

    f1.close()

from hw4 import *
from hashTableCorrect import *
import logging

def main():
    if prob1() == 0:
        print("****************************************************************#1 ternarySearch [PASSED]\n")
    else:
        print("*****************************************************************#1 ternarySearch [ERROR]\n")
    if prob2() == 0:
        print("*************************************************************#2 ternarySearchRec [PASSED]\n")
    else:
        print("**************************************************************#2 ternarySearchRec [ERROR]\n")
    if prob3() == 0:
        print("*********************************************************#3 hashtable put method [PASSED]\n")
    else:
        print("*********************************************************#3 hashtable put method [ERROR]\n")


def prob1():
    flag = 0
    a1 = [1,2,3,4]
    a2 = [4,7,89,100,124,3456,3568456,23423121]
    a3 = [n for n in range(0,50)]

    try:
        if ternarySearch(a1, 4) != True:
            flag += 1
        if ternarySearch(a1, 0) != False:
            flag += 1
        if ternarySearch(a2, 9) != False:
            flag += 1
        if ternarySearch(a2, 3568456) != True:
            flag += 1
        if ternarySearch(a3, 27) != True:
            flag += 1
        if ternarySearch(a3, 87) != False:
            flag += 1
        return flag
    except:
        return crash(flag)

def prob2():
    flag = 0
    a1 = [1,2,3,4]
    a2 = [4,7,89,100,124,3456,3568456,23423121]
    a3 = [n for n in range(0,50)]

    try:
        if ternarySearchRec(a1, 4) != True:
            flag += 1
        if ternarySearchRec(a1, 0) != False:
            flag += 1
        if ternarySearchRec(a2, 9) != False:
            flag += 1
        if ternarySearchRec(a2, 3568456) != True:
            flag += 1
        if ternarySearchRec(a3, 27) != True:
            flag += 1
        if ternarySearchRec(a3, 87) != False:
            flag += 1
        return flag
    except:
        return crash(flag)


def prob3():
    flag = 0
    x=HashTable()
    y=HashTableCorrect(x.size)
    try:
        for i in range(1,x.size+1):
            x[i] = i**2
            y[i] = i**2

        if x.slots != y.slots:
            print("Slots mismatch")
            flag += 1
        if x.data != y.data:
            print("Data Mismatch")
            flag += 1
        if x.size != y.size:
            print("Size mismatch")
            flag += 1

        return flag

    except:
        return crash(flag)



def crash(flag):
    logging.exception("_____crashed!")
    flag += 1
    return flag

if __name__ == "__main__":
    insertHashTableClass()
    main()