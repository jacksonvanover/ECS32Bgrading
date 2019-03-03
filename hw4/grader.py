from hw4 import *
from hashTableCorrect import *
import logging

def insertHashTableClass():
    # open student's hw4 file
    f1 = open("hw4.py", 'r+')

    # read in students code
    f1.seek(0,0)
    studentCode = f1.readlines()
    f1.seek(0,0)

    # # check if student's code has gone through the grader once already
    # for line in studentCode:
    #     if "# pineapple" in line:
    #         return

    # open the Incomplete HashTable Class file
    f2 = open("hashTableIncomplete.py", 'r')

    # read in hashTableClass
    f2.seek(0,0)
    hashTableClass = f2.readlines()
    f2.close()

    i = 0
    j = 0
    flag = False

    # until reading the line containing the put function header
    while "def put(" not in studentCode[i] and i < len(studentCode):

        # if the student's code contains a hashtable class, don't write any of those lines
        if "class Hash" in studentCode[i] or "class hash" in studentCode[i]:
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
            print("Was expecting True but got False")
            flag += 1
        if ternarySearch(a1, 0) != False:
            print("Was expecting False but got True")
            flag += 1
        if ternarySearch(a2, 9) != False:
            print("Was expecting False but got True")
            flag += 1
        if ternarySearch(a2, 3568456) != True:
            print("Was expecting True but got False")
            flag += 1
        if ternarySearch(a3, 27) != True:
            print("Was expecting True but got False")
            flag += 1
        if ternarySearch(a3, 87) != False:
            print("Was expecting False but got True")
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
            print("Was expecting True but got False")
            flag += 1
        if ternarySearchRec(a1, 0) != False:
            print("Was expecting False but got True")
            flag += 1
        if ternarySearchRec(a2, 9) != False:
            print("Was expecting False but got True")
            flag += 1
        if ternarySearchRec(a2, 3568456) != True:
            print("Was expecting True but got False")
            flag += 1
        if ternarySearchRec(a3, 27) != True:
            print("Was expecting True but got False")
            flag += 1
        if ternarySearchRec(a3, 87) != False:
            print("Was expecting False but got True")
            flag += 1
        return flag
    except:
        return crash(flag)


def prob3():
    flag = 0
    x=HashTable()
    y=HashTableCorrect(x.size)
    ogSize = x.size
    try:
        for i in range(1,x.size+2):
            x[i**2] = "data{}".format(i)
            y[i**2] = "data{}".format(i)
            lastData = "data{}".format(i)

        if x.size != y.size:
            print("<<Resize mismatch>>")
            print("(Original hashtable size was {})".format(ogSize))
            print("Was expecting resize to {} but instead got resize to {}".format(y.size, x.size))
            print()
            flag += 1
        if x.slots != y.slots:
            print("<<Slots mismatch>>")
            print("Was expecting {}".format(y.slots))
            print("Instead, got  {}".format(x.slots))
            print()
            flag += 5
        if x.data != y.data:
            print("<<Data Mismatch>>")
            print("Was expecting {}".format(y.data))
            print("Instead, got  {}".format(x.data))
            print()
            flag += 5
        if flag > 3:
            print("Note: last item to be placed that is causing the resize is [144:data12]\n")
        if lastData not in x.data:
            print("<<Put method didn't ultimately place the last item that caused the resize, {}, possibly only reason for mismatch?>>".format(lastData))
            print()
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