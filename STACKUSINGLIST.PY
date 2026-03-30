def push():
    n=int(input('enter element to insert'))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print(n,'is inserted')
def pop():
    if len(stack)==0:
        print('stack is empty')  
    else:
        rem=stack.pop(0)
        print(rem,'is deleted')
def display():
    if len(stack)==0:
        print('stack is empty')
    else:
        print('elements are:')    
        for ele in stack:
            print(ele)                    

stack=list()  
while(1):
    print('enter the below options \n1-push operation \n2-pop operation \n3-display operation \nenter any key to exit')
    n=int(input('enter your option'))
    if n==1:
        push()
    elif n==2:
        pop()
    elif n==3: 
        display()
    else:
        print('option is not avilable')
        break          
