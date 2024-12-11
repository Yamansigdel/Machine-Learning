#if operator

"""if (condition):
          --------         
                     """

# x=int(input('Enter any number:'))
# if (x%3==0):
#     print('It is multiple of 3')
# elif(x%7==0):
#     print('It is multiple of  7')
# elif(x%11==0):
#     print('It is multiple of 11')
# else:
#     print('Not a multiple of 3,7 and 11')




# x= int(input("Enter a number: "))
# y=int (input("Enter a number: "))
# z=input("Enter opr: ")

# if z=="sum":
#     c=x+y
# elif z=="diff":
#     c=x-y

# print(f'{z} of x and y is {c}')


"""for var in range(start,end,step):

                    print (var)
                                    """


# even_numbers=[]

# for i in range(0,101,2):
#     even_numbers.append(i)

# print(even_numbers)
# from random import randint

# while True:
#     x=randint(1,6)
#     if(x%6!=0 or x%1!=0):
#         print(x)
#         break


#funtions


#function definition
# def func():
#     print('Hello World!!')


# func()  #this is func calling
# from random import randint

# def guess(x):
#         y= randint(1,10)
#         if x==y:
#                 return(y,(f'Your guess {x} is correct with number {y}; try again !!'))
#         else:
#                 return (y,f'Your guess {x} is not correct with number {y}; try again !!')
                 
# i=0
# while (True):

#     z=int(input('Enter a number between 1-10: '))
#     i+=1
#     a,b=guess(z)
#     if a==z:
#            print(b,f'You matched in {i} times')
#            break
#     else:
#            print(b)

# def maximum(x):
#     return (max(x))


# x=[1,2,3,4,5,8]
# z=maximum(x)
# print(f'maximum in x is {z}')
      
      

# def max_finder(**args):
#     print(args)

# max_finder(a=10,b=20,c=30)


#design a function that uses kwargs to display these records.

# def display(**args):    
#     print(args)

# display(name='anup stark', dept= 'bei',bank='None', birthday= 'Ashar 25',age=16)

