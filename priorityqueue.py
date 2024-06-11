prioqueue=[]
n=int(input("Enter maximum queue size:"))

def insert(data,prio):
    if isFull():
        print("Queue is full")
    else:
        prioqueue.append((data,prio))
        prioqueue.sort(reverse=True)
        print(f"({data,prio}) inserted")

def delete():
    if isEmpty():
        print("Queue is empty")
    else:
        a=prioqueue.pop(0)
        print(f"Deleted {a}")

def isEmpty():
    if len(prioqueue)==0:
        return True
    else:
        return False
    

def isFull():
    if len(prioqueue)==n:
        return True
    else:
        return False
    
def front():
    if not isEmpty():
        print(f"Element with highest priority is {prioqueue[0]}")
    else:
        print("Queue is empty")

def rear():
    if not isEmpty():
        print(f"Element with lowest priority is {prioqueue[-1]}")
    else:
        print("Queue is empty")

def size():
    print(f"Queue size is {len(prioqueue)}")

while True:
    ch=int(input("Enter your choice:\n1.insert\n2.delete\n3.isEmpty\n4.isFull\n5.Front\n6.Rear\n7.Size\n8.Print\n9.Break\n"))
    if ch==1:
        data=int(input("Enter data to be inserted:"))
        prio=int(input("Enter priority of data:"))
        insert(prio,data)
    elif ch==2:
        delete()
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
        print(prioqueue)
    elif ch==9:
        break
    else:
        print("Invalid choice")