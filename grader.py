
with open("hw2.py", 'r+') as f:
    if f.readline().strip() != "from nodes import *":
        f.seek(0,0)
        content = f.read()
        f.seek(0, 0)
        f.write("from nodes import *".rstrip('\r\n') + '\n' + content)

from hw2 import *
#from UnorderedList import *
import logging

def main():
    if prob1() == 0:
        print("**************************************QueueX [PASSED]\n")
    else:
        print("**************************************QueueX [ERROR]\n")

    if prob2() == 0:
        print("**************************************slice [PASSED]\n")
    else:
        print("**************************************slice [ERROR]\n")

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
        print("\nConstructor")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty mismatch")
            flag += 1
    except:
        print("\nisEmpty")
        flag = crash(flag)
    
    try:
        x.enqueue(1)
        x.enqueue(2)
        x.enqueue(3)
        x.enqueue(4)
        x.enqueue(5)
    except:
        print("\nenqueue")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize mismatch")
            flag += 1
    except:
        print("\nsize")
        flag = crash(flag)

    try:
        if x.dequeue() != 1:
            print("\ndequeue mismatch")
            flag += 1
    except:
        print("\ndequeue")
        flag = crash(flag)

    return flag

def prob2():
    try:
        x = UnorderedList()
        x.add(5)
        x.add(4)
        x.add(3)
        x.add(2)
        x.add(1)
        x.add(0)
        y = x.slice(0,4)
        if y.head.getData() != 0 or y.head.getNext().getData() != 1 or y.head.getNext().getNext().getData() != 2 or y.head.getNext().getNext().getNext().getData() != 3:
            print("slice mismatch")
            return 1
    except:
        crash(1)
        return 1

    return 0

def prob3():
    flag = 0
    try:
        x = Stack()
    except:
        print("\nConstructor")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty mismatch")
            flag += 1
    except:
        print("\nisEmpty")
        flag = crash(flag)
    
    try:
        x.push(5)
        x.push(4)
        x.push(3)
        x.push(2)
        x.push(1)
    except:
        print("\npush")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize mismatch")
            flag += 1
    except:
        print("\nsize")
        flag = crash(flag)

    try:
        if x.pop() != 1:
            print("\npop mismatch")
            flag += 1
    except:
        print("\npop")
        flag = crash(flag)

    try:
        if x.peek() != 2:
            print("\npeek mismatch")
            flag += 1
    except:
        print("\npeek")
        flag = crash(flag)

    return flag

def prob4():
    flag = 0
    try:
        x = Queue()
    except:
        print("\nConstructor")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty mismatch")
            flag += 1
    except:
        print("\nisEmpty")
        flag = crash(flag)
    
    try:
        x.enqueue(1)
        x.enqueue(2)
        x.enqueue(3)
        x.enqueue(4)
        x.enqueue(5)
    except:
        print("\nenqueue")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize mismatch")
            flag += 1
    except:
        print("\nsize")
        flag = crash(flag)

    try:
        if x.dequeue() != 1:
            print("\ndequeue mismatch")
            flag += 1
    except:
        print("\ndequeue")
        flag = crash(flag)

    return flag

def prob5():
    flag = 0
    try:
        x = Deque()
    except:
        print("\nConstructor")
        flag = crash(flag)
    try:
        if x.isEmpty() != True:
            print("\nisEmpty mismatch")
            flag += 1
    except:
        print("\nisEmpty")
        flag = crash(flag)
    
    try:
        x.addFront(3)
        x.addFront(2)
        x.addFront(1)
    except:
        print("\naddFront")
        flag = crash(flag)

    try:
        x.addRear(4)
        x.addRear(5)
    except:
        print("\naddRear")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize mismatch")
            flag += 1
    except:
        print("\nsize")
        flag = crash(flag)

    try:
        if x.removeFront() != 1:
            print("\nremoveFront mismatch")
            flag += 1
    except:
        print("\nremoveFront")
        flag = crash(flag)

    try:
        if x.removeRear() != 5:
            print("\nremoveRear mismatch")
            flag += 1
    except:
        print("\nremoveRear")
        flag = crash(flag)

    return flag
    
def prob6():
    flag = 0
    try:
        x = Deque2()
    except:
        print("\nConstructor")
        flag = crash(flag)
    
    try:
        if x.isEmpty() != True:
            print("\nisEmpty mismatch")
            flag += 1
    except:
        print("\nisEmpty")
        flag = crash(flag)
    
    try:
        x.addFront(3)
        x.addFront(2)
        x.addFront(1)
    except:
        print("\naddFront")
        flag = crash(flag)

    try:
        x.addRear(4)
        x.addRear(5)
    except:
        print("\naddRear")
        flag = crash(flag)

    try:
        if x.size() != 5:
            print("\nsize mismatch")
            flag += 1
    except:
        print("\nsize")
        flag = crash(flag)

    try:
        if x.removeFront() != 1:
            print("\nremoveFront mismatch")
            flag += 1
    except:
        print("\nremoveFront")
        flag = crash(flag)

    try:
        if x.removeRear() != 5:
            print("\nremoveRear mismatch")
            flag += 1
    except:
        print("\nremoveRear")
        flag = crash(flag)

    return flag

def crash(flag):
    logging.exception("_____crashed!")
    flag += 1
    return flag

if __name__ == "__main__":
    main()