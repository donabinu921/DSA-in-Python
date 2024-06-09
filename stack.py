stack=[]

def push(elem):
    stack.append(elem)

def pop():
    if len(stack)==0:
        print("Stack is empty")
        return None
    a=stack.pop(-1)
    return a

def peek():
    if len(stack)==0:
        print("Stack is empty")
        return None
    return stack[-1]

def search(ele):
    if len(stack)==0:
        print("Stack is empty")
        return
    if ele in stack:
        print(f"Element in stack at index {stack.index(ele)}")
    else:
        print("Element not in stack")

while True:
    ch=int(input("Enter your choice:\n1.Push\n2.Pop\n3.Print\n4.Peek\n5.Search\n6.Break\n"))
    if ch==1:
        elem=int(input("Enter the element to be pushed:"))
        push(elem)
        print("Pushed",elem)
    elif ch==2:
        b=pop()
        print("Popped",b)
    elif ch==3:
        print(stack)
    elif ch==4:
        print("Element at top is",peek())
    elif ch==5:
        c=int(input("Enter element to be searched for:"))
        search(c)
    elif ch==6:
        break
    else:
        print("Invalid choice")

    
    
    