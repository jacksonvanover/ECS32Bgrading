from hw5 import *
import logging

x_1 = [1,4,2,5,3,6,7,9,8,10]
x_2 = [1,4,2,5,-3,6,-7,9,8,0]
x_3 = [1,4,2,5,-3,6,-7,9,8,0]
correct = [-7,-3,0,1,2,4,5,6,8,9]
pancakeCorrect = [1,2,3,4,5,6,7,8,9,10]

def main():
    if prob1() == 0:
        print("****************************************************************#1 PancakeSort [PASSED]\n")
    else:
        print("*****************************************************************#1 PancakeSort [ERROR]\n")
    if prob2() == 0:
        print("*****************************************************************#2 BubbleSort [PASSED]\n")
    else:
        print("******************************************************************#2 BubbleSort [ERROR]\n")
    if prob3() == 0:
        print("******************************************************************#3 MergeSort [PASSED]\n")
    else:
        print("*******************************************************************#3 MergeSort [ERROR]\n")

def prob1():
    flag = 0
    try:
        if pancakeSort(x_1):
            y_1 = pancakeSort(x_1)

            if y_1 != pancakeCorrect:
                flag += 1

        else:
            if x_1 != pancakeCorrect:
                flag += 1

        return flag

    except:
        return crash(flag)

def prob2():
    flag = 0
    try:
        if bubbleSort(x_2):
            y_2 = bubbleSort(x_2)

            if y_2 != correct:
                flag += 1
        else:
            if x_2 != correct:
                flag += 1
        return flag
    except:
        return crash(flag)

def prob3():
    flag = 0
    try:
        if mergeSort(x_3):
            y_3 = mergeSort(x_3)

            if y_3 != correct:
                flag += 1
        else:
            if x_3 != correct:
                flag += 1
        return flag
    except:
        try:
            if mergeSort(x_3, 0, len(x_3)-1):
                y_3 = mergeSort(x_3, 0, len(x_3)-1)

                if y_3 != correct:
                    flag += 1

            else:
                if x_3 != correct:
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