with open("hw2.py", 'r+') as f:
    if f.readline().strip() != "from nodes import *":
        f.seek(0,0)
        content = f.read()
        f.seek(0, 0)
        f.write("from nodes import *".rstrip('\r\n') + '\n' + content)

from hw2 import *
import logging

def main():
    if prob1() == 0:
        print("**************************************QueueX [PASSED]\n")
    else:
        print("**************************************QueueX [ERROR]\n")

    if prob3() == 0:
        print("**************************************Stack [PASSED]\n")
    else:
        print("**************************************Stack [ERROR]\n")

    if prob4() == 0:
        print("**************************************Queue [PASSED]\n")
    else:
        print("**************************************Queue [ERROR]\n")  

    if prob5() == 0:
        print("**************************************Deque [PASSED]\n")
    else:
        print("**************************************Deque [ERROR]\n")

    if prob6() == 0:
        print("**************************************Deque2 [PASSED]\n")
    else:
        print("**************************************Deque2 [ERROR]\n")        

def prob1():
    flag = 0
    try:
        x = QueueX()
    except:
        print("\nConstructor crash")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty Error")
            flag += 1
    except:
        print("\nisEmpty crash")
        flag = crash(flag)
    
    try:
        x.enqueue(1)
        x.enqueue(2)
        x.enqueue(3)
        x.enqueue(4)
        x.enqueue(5)
    except:
        print("\nenqueue crash")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize Error")
            flag += 1
    except:
        print("\nsize crash")
        flag = crash(flag)

    try:
        if x.dequeue() != 1:
            print("\ndequeue error")
            flag += 1
    except:
        print("\ndequeue crash")
        flag = crash(flag)

    return flag

def prob3():
    flag = 0
    try:
        x = Stack()
    except:
        print("\nConstructor crash")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty Error")
            flag += 1
    except:
        print("\nisEmpty crash")
        flag = crash(flag)
    
    try:
        x.push(5)
        x.push(4)
        x.push(3)
        x.push(2)
        x.push(1)
    except:
        print("\npush crash")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize Error")
            flag += 1
    except:
        print("\nsize crash")
        flag = crash(flag)

    try:
        if x.pop() != 1:
            print("\npop error")
            flag += 1
    except:
        print("\npop crash")
        flag = crash(flag)

    return flag

def prob4():
    flag = 0
    try:
        x = Queue()
    except:
        print("\nConstructor crash")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty Error")
            flag += 1
    except:
        print("\nisEmpty crash")
        flag = crash(flag)
    
    try:
        x.enqueue(1)
        x.enqueue(2)
        x.enqueue(3)
        x.enqueue(4)
        x.enqueue(5)
    except:
        print("\nenqueue crash")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize Error")
            flag += 1
    except:
        print("\nsize crash")
        flag = crash(flag)

    try:
        if x.dequeue() != 1:
            print("\ndequeue error")
            flag += 1
    except:
        print("\ndequeue crash")
        flag = crash(flag)

    return flag

def prob5():
    flag = 0
    try:
        x = Deque()
    except:
        print("\nConstructor crash")
        flag = crash(flag)
    try:
        if x.isEmpty() != True:
            print("\nisEmpty Error")
            flag += 1
    except:
        print("\nisEmpty crash")
        flag = crash(flag)
    
    try:
        x.addFront(3)
        x.addFront(2)
        x.addFront(1)
    except:
        print("\naddFront crash")
        flag = crash(flag)

    try:
        x.addRear(4)
        x.addRear(5)
    except:
        print("\naddRear crash")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize Error")
            flag += 1
    except:
        print("\nsize crash")
        flag = crash(flag)

    try:
        if x.removeFront() != 1:
            print("\nremoveFront error")
            flag += 1
    except:
        print("\nremoveFront crash")
        flag = crash(flag)

    try:
        if x.removeRear() != 5:
            print("\nremoveRear error")
            flag += 1
    except:
        print("\nremoveRear crash")
        flag = crash(flag)

    return flag
    
def prob6():
    flag = 0
    try:
        x = Deque2()
    except:
        print("\nConstructor crash")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty Error")
            flag += 1
    except:
        print("\nisEmpty crash")
        flag = crash(flag)
    
    try:
        x.addFront(3)
        x.addFront(2)
        x.addFront(1)
    except:
        print("\naddFront crash")
        flag = crash(flag)

    try:
        x.addRear(4)
        x.addRear(5)
    except:
        print("\naddRear crash")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize Error")
            flag += 1
    except:
        print("\nsize crash")
        flag = crash(flag)

    try:
        if x.removeFront() != 1:
            print("\nremoveFront error")
            flag += 1
    except:
        print("\nremoveFront crash")
        flag = crash(flag)

    try:
        if x.removeRear() != 5:
            print("\nremoveRear error")
            flag += 1
    except:
        print("\nremoveRear crash")
        flag = crash(flag)

    return flag

def crash(flag):
    logging.error("_____crashed!")
    flag += 1
    return flag

if __name__ == "__main__":
    main()