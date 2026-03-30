def enqueue():
    n=int(input('enter the number to be inserted into queue'))
    queue.append(n)

def dequeue():
    if len(queue)==0:
        print('stack is empty')
    else:
        rem=queue.pop(0)
        print(rem,'is removed from the stack') 
        print()
def display():
    if len(queue)==0:
        print('Queue is empty') 
    else:
        print('elemnts in queue are:') 
        for ele in queue:
            print(ele,end=' ')
    print('front element is',queue[0]) 
    print('rear element is',queue[-1]) 

queue=list() 
while True:
    print('enter the below options \n1-push operation \n2-pop operation \n3-display operation \nenter any key to exit')
    n=int(input('enter your option'))
    if n==1:
        enqueue()
    elif n==2:
        dequeue()
    elif n==3: 
        display()
    else:
        print('option is not avilable')
        break          

                    