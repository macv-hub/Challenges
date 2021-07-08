import time
import turtle

#EXERCISES FROM THINK PYTHON CHAPTER 5

t = turtle.Turtle()

def timehs():
    t = time.time()
    days = t//(60*60*24)
    hours = (t%(60*60*24))//(60*60)
    min = ((t%(60*60*24))%(60*60))//60
    sec = (((t%(60*60*24))%(60*60))//60)%60
    print(time.gmtime(time.time()))
    return f"{hours} hours:{min} min:{sec} sec + {days} days since the epoch"
    
def fermat(a,b,c,n):
    if a**n + b**n == c**n:
        return print(f"Holy smokes, Fermat was wrong!{a,b,c,n}")
    else:
        return print(f"Nope, that doesn\'t work {a,b,c,n}")

# Python program to demonstrate
# passing dictionary as argument
  
  
# A function that takes dictionary
# as an argument
def func(d):
      
    for key in d:
        print("key:", key, "Value:", d[key])
          
# # Driver's code
# D = {
#     'fyk':1, 
#     'fck':2, 
#     'c':3
#     }
# func(D)

# print(timehs())
# fermat(0,0,0,1000)

def is_triangle(a,b,c):
    sticks = (a,b,c)
    total = sum(sticks)
    base = max(sticks)
    if total - 2 * base >= 0:
        print('Yes')
    else:
        print('No')

def is_triangle2(a,b,c):
    sticks = (a,b,c)
    if a > b + c or b > a + c or c > a + b:
        print('Not possible')
    else:
        print('Yes')

def check_triangle():
    a = int(input('Insert a: \n'))
    b = int(input('Insert b: \n'))
    c = int(input('Insert c: \n'))
    return is_triangle2(a, b, c)

def recurse(n,s):
    '''Function that takes 2 arguments n and s and prints n**2+s-(n+1) if that's what you need. 
    Not very useful but hey it is a recursive function!'''
    try:
        if n ==0:
            print(s)
        else:
            recurse(n-1, n+s)
    except RecursionError:
        print('\nn can\'t be negative you punk!\n')

def draw(t, length, n):
    if n == 0:
        return
    angle = 60
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def snowflake(t, length, n):
    for i in range(n):
        draw(t,length,n)
        t.lt(360/n)

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake2(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)

# draw(t,10,5)
# koch(t,300)
snowflake2(t, 300)
# snowflake(t, 5, 3)
# is_triangle(1,1,1)
# is_triangle2(10, 1, 1)
# check_triangle()
# recurse(3, 0)
# recurse(-1, 0)
# help(recurse)