#Write a program to convert kg to g. (Input 56kg print in grams)

def covertkgtog(n):
    print(n*1000)




#2. Write a program to covert temperature from degree C to F. (Input 80C)
#(80°C × 9/5) + 32 = 176°F

def convertctof(n):
    print(n*(9/5)+32)



#3. Declare and initialize 3 three variable and print the biggest number.
a=[1,2,3]
def bignumber(a):
    print(max(a))



#4. Write a java program that performs the following tasks.
#a. Store a number in a variable
#b. If value is not in range (100-1000) prints wrong number else follows
#the steps
# c. Check even or odd
# d. If even divide the number by 3 and print the remainder
# e. If odd divide the number by 2 and print the remainder.

def fun(a):
    if a not in range(100,1000):
        print("Wrong Number")
    if a%2==0:
        print("Even")
        print(a%3)
    else:
        print("odd")
        print(a%2)

fun(20)






# 5. Declare & initialize a number. Check whether the number is in range 0-100
# or not. If not in range print invalid input. Else – if the number is in range 90-
# 100 then print Super Smart, 80-90 print Smart,70-80 print smart enough,
# 60-70 print just smart, 35-60 print no smart, 0-35 print dump.

def fun1(a):
    if a not in range(0,100):
        print("Invalid Input")
    elif a in range(90,100):
        print("Supersmart")
    elif a in range(80,90):
        print("Smart")
    elif a in range(70,80):
        print("Smart enough")
    elif a in range(60, 70):
        print("just Smart")
    elif a in range(35, 60):
        print("No Smart")
    elif a in range(0,35):
        print("Dump")

# 6. Write a program to perform simple math based on the user inputs by using
# Switch condition.(+ , - , * , /)


# 7. Write a program to print “SEEKHO BIGDATA”for 60 times.

print("SEEKHOBIGDATA\n"*60)

# 8. Write a program to print all numbers which are divisible by 11 from 250 to
# 550.

for i in range(249,550):
    if(i%11==0):
        print(i)
        i=i+1
    else: i=i+1


# 9. Write a program to sum all the numbers from 56 to 153.
def fun2():
    k=0
    for i in range(56,153):
        k=k+i
    print(k)

fun2()



# 10. Write a program to print all even numbers in range 700 to 900.

def even():
    for i in range(700,900):
        if(i%2==0):
            print(i)

# 11. Write a program to print all odd numbers from 251 to 51. like (251,
# 249,...51)
def odd():
    for i in range(700,900):
        if(i%2!=0):
            print(i)


# 12. Write a Program to print the count of the even numbers between the given
# range?

def counteven():
    c=0
    for i in range(1,100):
       if(i%2==0):
           c=c+1
    print(c)


# 13. Write a program to print alternate even numbers from 20 to 140. Like
# (20,24,28...)
def alteven():
    for i in range(20,140,4):
        if(i%2==0):
            print(i)
alteven()
# Seekho Bigdata Institute
# 14. Write a program to print alternate even numbers from 20 to 140. Like
# (22,26,30...)

def alteven1():
    for i in range(20,140,4):
        if(i%2==0):
            print(i+2)
alteven1()


# 15. Print following series 2*3,3*4,4*5,......16*17 (Print in two ways – patter
# & multiplied value)

def series():
    for i in range(2,17):
        print(str(i)+"*"+str(i+1))
    for i in range(2,17):
        print(i*(i+1))

# 16. Write a program to sum all even numbers between 382 and 582.
def sumeven():
    s=0
    for i in range(382,583,2):
        s=s+i
    print(s)

# 17. Write a Program to print the all alphabets by using character Variable?


# 18. Write a program to find the average of 24,26,28,.....100.
def avg():
    s=0
    c=0
    for i in range(24,101,2):
        s=s+i
        c=c+1
    print(s/c)
# 19. Write programs to sum of the following Series. 52 + 62 + 72
# +..........+1022.
def sumofseries():
    s=0
    for i in range(52,1023,10):
        s=s+i
    print(s)

# 20. Write a program to print A, B alternatively for 100 times. Ex: (A, B, A, B,
# A,B...)

print("A,B,"*100)

# 21. Write a program to print the series : 10@9,9@8,8@7.......-5@-6
def serieswith():
    for i in range(10,-6,-1):
        print(str(i)+"@"+str(i-1)+'',end='')
serieswith()

# 22. Write programs to print the following series. 100,200,300........10000

def serieshundred():
    for i in range(0,10000,100):
        print(i+100)

serieshundred()
# 23. Write programs to print the following series. 5^2, 7^2,9^2.....25^2

for i in range(5,26,2):
    print(str(i)+'^'+str(2), end='')
# 24. Write programs to print the following series. 5,10,5,10,5,10,5 for 7 times
print("\n")
print("5,10,5,10,5,10,5"*7)
# 25. Write programs to print the following series. 5*4,5*3,5*2,......5*(-12)
# (Print in two ways – patter & multiplied value)

for i in range(4,-13,-1):
    print(str(5)+"*"+str(i))
# 26. Write programs to print the following series.
# 1,even,3,even,5,even,.......35,even

for i in range(1,36,2):
    print(str(i)+','+'even'+',',end='')
# 27. Write programs to print the following series. 1,2,factor of three,4,5,factor

print('\n')
for i in range(1,30):
    if i%3==0:
        print("factor of three,",end='')
    else:
        print(str(i)+',',end='')
# of three, 7,8,factor of three,..........22,23,factor of three.
# 28. Write programs to print the following series. 1,3, divisible by five, 7,9,
# 11,13, divisible by five,.....21,23, divisible by five

for i in range(1,24,2):
    if i % 5 == 0:
        print("divisible by 5,", end='')
    else:
        print(str(i) + ',', end='')

# 29. Write programs to print the following series. 0.5^2, 0.7^2,0.9^2....5.1^2
def funcc():
    s=0.5
    e=5.1
    st=0.2
    for  i in range(s,e,st):
        print(str(i)+'^'+str(2))
# 30. Write a for loop that never ends?
#while True:
#    s=s+1
# 31. Write a Loop inside other loop and observe the execution flow?
def loopinloop():
    for i in range(1,10):
        for i in range(21,30):
           print(i)