queue=[]
n=int(input("Enter maximum queue size:"))

def enqueue(ele):
    if isFull():
        print("Queue is full")
    else:
        queue.append(ele)
        print(f"{ele} added to tail")

def dequeue():
    if isEmpty():
        print("Queue is empty")
    else:
        a=queue.pop(0)
        print(f"Popped {a} from head")

def isEmpty():
    if len(queue)==0:
        return True
    else:
        return False
    

def isFull():
    if len(queue)==n:
        return True
    else:
        return False
    
def front():
    if not isEmpty():
        print(f"Element at head is {queue[0]}")
    else:
        print("Queue is empty")

def rear():
    if not isEmpty():
        print(f"Element at rear is {queue[-1]}")
    else:
        print("Queue is empty")

def size():
    print(f"Queue size is {len(queue)}")

while True:
    ch=int(input("Enter your choice:\n1.Enqueue\n2.Dequeue\n3.isEmpty\n4.isFull\n5.Front\n6.Rear\n7.Size\n8.Print\n9.Break\n"))
    if ch==1:
        a=int(input("Enter an element to be enqueued:"))
        enqueue(a)
    elif ch==2:
        dequeue()
    elif ch==3:
        if isEmpty():
            print("Empty")
        else:
            print("Not empty")
    elif ch==4:
        if isFull():
            print("Full")
        else:
            print("Not full")
    elif ch==5:
        front()
    elif ch==6:
        rear()
    elif ch==7:
        size()
    elif ch==8:
        print(queue)
    elif ch==9:
        break
    else:
        print("Invalid choice")