
def even_odd_checker(x):
    if( x%2==0):
        print('It is even number')
    else:
        print('It is odd number')

def Calculator():
    
    def Sum(a,b):
        return(a+b)
    
    def Diff(a,b):
        return(a-b)
    
    def Mul(a,b):
        return(a*b)
    
    def Div(a,b):
        return(a/b)
    
    a=int(input('Enter two numbers: '))
    
    b=int(input('Enter two numbers: '))
    choice=input('Enter a choice(+, - , *, /): ')
    if choice=='+':
        print(Sum(a,b))
    elif choice=='-':
        print(Diff(a,b))
    elif choice=='*':
        print(Mul(a,b))
    else:
        print(Div(a,b))

import datetime
def Greeter():
    x=datetime.datetime.now().time()
    if x.hour < 12:
        print('Good morning')
    else:
        print('Good afternoon')

def Prime_num(n1=1,n2=100):
    x=[]
    for i  in range(n1,n2):
        count=0
        for j in range(1,i):
            if i % j==0:
                count+=1

        if count<2:
            x.append(i)
        
        
    print(f'prime numbers between {n1} and {n2} are: :{x}')

if __name__=="__main__":
    even_odd_checker(9)
    Calculator()
    Greeter()
    Prime_num()


