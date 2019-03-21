from hw6 import *
import logging

alist = [1,4,2,5,-3,6,-7,9,8]
correct = [-7,-3,1,2,4,5,6,8,9]

def main():
    if prob1() == 0:
        print("****************************************************************#1 heapSort [PASSED]\n")
    else:
        print("*****************************************************************#1 heapSort [ERROR]\n")

def prob1():
    flag = 0
    x = BinHeap()
    try:
        x.buildHeap(alist)
        try:
            test = x.heapsort()
        except:
            test = x.heapSort()

        if (x.heapList != correct):
            print("Was expecting {} but instead got {}".format(correct,x.heapList))
            flag += 1

        if (test is not None):
            print("Wasn't expecting a return from heapSort, but got {}".format(test))

        return flag
    except:
        try:
            try:
                test = x.heapsort(alist)
            except:
                test = x.heapSort(alist)

            if (x.heapList != correct):
                print("Was expecting {} but instead got {}".format(correct,x.heapList))
                flag += 1

            if (test is not None):
                print("Wasn't expecting a return from heapSort, but got {}".format(test))

            return flag

        except:
            return crash(flag)

def crash(flag):
    logging.exception("_____crashed!")
    flag += 1
    return flag

if __name__ == "__main__":
    main()