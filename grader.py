with open("hw2.py", 'r+') as f:
    if f.readline().strip() != "from nodes import *":
        f.seek(0,0)
        content = f.read()
        f.seek(0, 0)
        f.write("from nodes import *".rstrip('\r\n') + '\n' + content)

from hw2 import *

def main():
    if prob1() == 0:
        print("***QueueX [PASSED]\n")
    else:
        print("***QueueX [ERROR]\n")

    if prob3() == 0:
        print("***Stack [PASSED]\n")
    else:
        print("***Stack [ERROR]\n")

    if prob4() == 0:
        print("***Queue [PASSED]\n")
    else:
        print("***Queue [ERROR]\n")  

    if prob5() == 0:
        print("***Deque [PASSED]\n")
    else:
        print("***Deque [ERROR]\n")

    if prob6() == 0:
        print("***Deque2 [PASSED]\n")
    else:
        print("***Deque2 [ERROR]\n")        

def prob1():
    try:
        flag = 0
        x = QueueX()
        if x.isEmpty() is not True:
            print("isEmpty Error")
            flag += 1

        x.enqueue(1)
        x.enqueue(2)

        if x.items[0] != 1:
            print("enqueue error")
            flag += 1
        if x.size() != 2:
            print("size error")
            flag += 1

        x.enqueue(3)

        if x.items[len(x.items)-1] != 3:
            print("enqueue error")
            flag += 1

        if x.isEmpty() is True:
            print("isEmpty error")
            flag += 1

        if x.items != [1,2,3]:
            print("enqueue error")
            flag += 1

        if x.size() is not 3:
            print("size error")
            flag += 1

        if x.dequeue() != 1:
            print("dequeue error")
            flag += 1

        if x.items[0] != 2:
            print("enqueue or dequeue error")
            flag += 1

        return flag    

    except:
        print("_____crashed!")
        return 1

def prob3():
    try:
        flag = 0
        x = Stack()
        if x.isEmpty() != True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 0:
            print("size error")
            flag += 1
        x.push(1)
        x.push(2)
        if x.isEmpty() == True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 2:
            print("size error")
            flag += 1
        if x.peek() != 2:
            print("peek error")
            flag += 1
        x.push(3)
        if x.size() != 3:
            print("size error")
            flag += 1
        if x.pop() != 3:
            print("pop error")
            flag += 1
        if x.pop() != 2:
            print("pop error")
            flag += 1
        return flag

    except:
        print("_____crashed!")
        return 1

def prob4():
    try:
        flag = 0
        x = Queue()
        if x.isEmpty() != True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 0:
            print("size error")
            flag += 1
        x.enqueue(1)
        x.enqueue(2)
        if x.isEmpty() == True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 2:
            print("size error")
            flag += 1
        x.enqueue(3)
        if x.dequeue() != 1:
            print("dequeue error")
            flag += 1
        if x.dequeue() != 2:
            print("dequeue error")
            flag += 1
        return flag

    except:
        print("_____crashed!")
        return 1

def prob5():
    try:
        flag = 0
        x = Deque()

        if x.isEmpty() != True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 0:
            print("size error")
            flag += 1

        x.addFront(2)
        x.addFront(1)

        if x.isEmpty() == True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 2:
            print("size error")
            flag += 1
        
        x.addRear(3)
        x.addFront(0)
        
        if x.size() != 4:
            print("size error")
            flag += 1
        if x.removeFront() != 0:
            print("removeFront error")
            flag += 1
        if x.removeRear() != 3:
            print("removeRear error")
            flag += 1
        if x.removeRear() != 2:
            print("removeRear error")
            flag += 1
        if x.removeRear() != 1:
            print("removeRear error")
            flag += 1
        return flag

    except:
        print("_____crashed!")
        return 1

def prob6():
    try:
        flag = 0
        x = Deque2()

        if x.isEmpty() != True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 0:
            print("size error")
            flag += 1

        x.addFront(2)
        x.addFront(1)

        if x.isEmpty() == True:
            print("isEmpty Error")
            flag += 1
        if x.size() != 2:
            print("size error")
            flag += 1
        
        x.addRear(3)
        x.addFront(0)
        
        if x.size() != 4:
            print("size error")
            flag += 1
        if x.removeFront() != 0:
            print("removeFront error")
            flag += 1
        if x.removeRear() != 3:
            print("removeRear error")
            flag += 1
        if x.removeRear() != 2:
            print("removeRear error")
            flag += 1
        if x.removeRear() != 1:
            print("removeRear error")
            flag += 1
        return flag

    except:
        print("_____crashed!")
        return 1

if __name__ == "__main__":
    main()