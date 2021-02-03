# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:32:36 2021

@author: shail
"""
#%%

def name():
    print("Hello Plz enter your name! ")

#%%

def AC():
    r=""
    print("Enter the radius in cm"+r)
    AC()=3.14*r*2
    print("Area circle of radius" radius "is" area)

#%%
def at(b,h):
    areat = 0.5 * b * h
    print("The area of triangle having base ",b," and height ",h," is ",areatat)

          
#%% 
name = ' My name is "Shailee Patel"'
age = "I am studying at O'hio"
print(name)
print(age)

#%%
both = "My dog's name is \"Butters\""
print(both)

#%%
def ftoc(F):
    C = ((F/9)*5)/9
    print("Farehneit temperature pf ",F," is ",C," degree Celsius")
#%%
def ftoc(F):
    C = ((F-32)*5)/9
    print("Farehneit     temperature     of ",end='')
    print(F," is ",C," degree Celsius")


#%%

def ctof(C):
    F = ((C/5)*9)+32
    print("Celcius temperature of ",C," is ",F," degree Farenhiet")

#%%
fname = input("Enter your first name: ")
lname= input("Enter your last name: ")
print("Hello! ",fname,lname)
city=input("Enter the city you live in ")
fullname = fname +" "+ lname
print("Ohh you are ",fullname,"from",city)
print("Nice to meet you!")

#%%
x = 0
if x < 0 :
    print("X is negative")
elif x > 0 :
    print("X is positive")
else:
    print("X must be zero")

#%%
x = -1
if x < 0 :
    print("X is negative")
if x > 0 :
    print("X is positive")
else:
    print("X must be zero")
#%%
def abc(): 
    x = input("Enter the value of X ")
    if x < 0 :
        print("X is negative")
    if x > 0 :
        print("X is positive")
    else:
        print(" X must be zero")

#%%
def area(type_,x):
    if type_ =="circle":
        area= 3.14* x **2
        print("Area of ",type_," ",x," is ",area)
    elif type_=="square":
        area= x**2
        print("Area of ",type_," ",x," is ",area)
    else :
        print("I dont know the answer!")


#%%
def Abs(x):
    if x <= 0 :
        a = abs(x)  
        print("The absolute value of ",x," is ",a)
    else x >= 0 :
        print("The absolute value of ",x," is ",x)
    

#%%
def fatoce():
    f = int(input("Enter tempreture in fareheniet : "))
    c = 5*(f-32)/9
    print("The tempreture of Farheniet",f," in Celcius is ",c," degree celcius")

 #%%
def fatoce1():
    f = int(input("Enter tempreture in farheniet: "))
    if f: 
        if f.isdigit():
            c = 5*(f-32)/9
            print("The tempreture of Farheniet",f," in Celcius is ",c," degree celcius")
        else:
            print("vALID iNPUT")
#%%
def fatoce2():
    f = input("Enter tempreture in farheniet: ")
    if f and f.isdigit():
        fx = int(f)
        c = 5*(fx-32)/9
        print("The tempreture of Farheniet",f," in Celcius is ",c," degree celcius")
        print("Enter the vALID iNPUT")
    
#%%
f = input("Enter tempreture in farheniet: ")
if f and f.isdigit():
    fx = int(f)
    c = 5*(fx-32)/9
    print("The tempreture of Farheniet",f," in Celcius is ",c," degree celcius")
else:
    print("Enter the vALID iNPUT")

#%%
def intofe():
    inches= int(input("Enter inches: "))
    fe = int(inches/12)
    inc = abs((fe*12)-inches)
    print("The conversion of ",inches," is ",fe," feet and ",inc," inches")


#%%
def intofe1():
    inches= int(input("Enter inches: "))
    fe = int(inches/12)
    r = inches%12
    print("The conversion of ",inches," is ",fe," feet and ",r," inches")

#%%
def whl():
    c = input("Enter the starting number ")
    if c and c.isdigit():
        ct = int(c)
        while ct <=100:
            print("Count is ",ct)
            ct = ct+10            
        print("Loop is over")
    else:
        print("Enter the valid Number")
        
#%%
def countdown():
    cd = input("Enter the number from the count down is to be done ")
    if cd and cd.isdigit():
        cd = int(cd)
        if cd <= 100:         
                print("Countdown from ",cd," is ")
                while cd>=0:
                    print(" ",cd,end=" " )
                    cd = cd - 1
                print("Count down is now finally over!")
        else:
            print("Please enter the number below 100.")  
    else:
            print("Enter a valid number below 100. Thank you!")

#%%          
def ran():
    r = int(input("Enter the first number : "))
    for r in range(r,100,5):
        print(r,end=" ")
    print("Range is over!")
    
#%%
def rancd():
    cd = input("Enter the number from the count down is to be done ")
    if cd and cd.isdigit():
        cd = int(cd)
        if cd <= 100:         
                print("Countdown from ",cd," is ")
                for cd in range(100,0,-1):
                    print(cd,end=" ")
                print("Count down is now finally over!")
        else:
            print("Please enter the number below 100.")  
    else:
            print("Enter a valid number below 100. Thank you!")


#%%
def L():
    List = ["Empty","a","b","c","d","e","f"]
    print("""1. For getting name of the student
          2. For knowing the person is on list 
          3. For knowing the total range of roll number
          4. For Adding the student to list""")
    IN = int(input("Enter the command from above :")
    if IN == 1 or 2 or 3 or 4
        if IN == 1:
            R = int(input("Enter the roll number :"))
            if R == 0:
                print("Enter a valid roll number. This roll number is not assigned")
            else:
                R = lis[R]
                print("The name of roll number is ",R)
        elif IN == 2:
            N = input("Enter the name of the person you want to check ")
            N in List
        elif IN == 3:
            print("The range of roll number is from 0 to",(len(List)-1))
        else:
            A = input("Enter the name of the student you wish to add: ")
            List.append(A)
    else:            
        print("Please enter a valid input")


#%%
def L():
    List = ["Empty","a","b","c","d","e","f"]
    i = int(input("Enter the command from above :",end="\n"
            " 1. For getting name of the student",end="\n"
            " 2. For knowing the person is on list",end="\n"
            " 3. For knowing the total range of roll number",end="\n"
            " 4. For Adding the student to list",end="\n")
    if i == 1:
        r = int(input("Enter the roll number: "))
        if r == 0:
            print("Enter a valid roll number. This roll number is not assigned")
        else:
            ro = lis[r]
            print("The name of roll number is ",ro)
    elif IN == 2:
        N = input("Enter the name of the person you want to check ")
        N in List
    elif IN == 3:
        print("The range of roll number is from 0 to",(len(List)-1))
    else:
        A = input("Enter the name of the student you wish to add: ")
        a = List.append(A)
        print(List)
        

#%%
def a():
    List = ["Empty","a","b","c","d","e","f"]
    A = input("Enter the name of the student you wish to add: ")
    a = List.append(A)
    print(List)


#%%
def who(lis):
    if "bear" in lis:
        print("This is bear")
    if "rat" in lis:
        print("The animal is rat")
    if "iris" in lis or "rose" in lis:
        print("these are flowers")
    if "horse" is not lis:
        print("The horse is not in list")
    print("The list has ",len(lis)," number of items")
    

#%%
l=["lion"]
b=["bear"]
lb=["lion","bear"]
lbd=["lion","bear","daisy"]

#%%          
def ca(alist):
    ct = 0
    for e in alist:
        e = input" Letter :"
        e == e
        ct = 1 + ct
    print(ct)

#%%
lisa= ["a","d","f","e","d","g","y","r","s","d","a","e","f","f","g"]

#%%

def ca1(alis):
    ct = 0
    a = input("letter : ")
    for o in alis:        
        if o == a:
            ct = 1 + ct
    print("The ",a," in letter is ",ct)

#%%
nlis=[2,4,8,105,210,-3,47,8,33,1]
nlis2=[3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4]

def avg():
    n = nlis
    c = 0
    for i in range(0,len(n)):
        print(n[i])
        c = c + 1
    for avg in nlis:
        avg = sum(nlis)/len(nlis) 
    print("Avg of",nlis,"is",avg," count of number is",len(nlis))
    
    n = nlis2
    c = 0
    for i in range(0,len(n)):
        print(n[i])
        c = c + 1
    for avg in nlis2:
        avg = sum(nlis2)/len(nlis2) 
    print("Avg of",nlis2,"is",avg," count of number is",len(nlis2))         

    
#%%
GJ = ["Vadodara","Ahemdabad","Rajkot","Surat","Bharuch"]
RJ = ["Jaipur","Udaipur","Jaisalmer","Ajmer","Kota"]
MP = ["Bhopal","Ujjain","Khandwa","Bhandavgarh","Khajuro"]
MH = ["Mumbai","Pune","Jhansi","Nasik","Kolhapur"]


def place(s):
    i = 0
    for state in range(0,len(s)):
        print(i+1," - ",s[i])
        i = i + 1
    
    

#%%
def pro():
    n1 = int(input("Enter number 1 : "))
    n2 = float(input("Enter number 2 : "))
    print("The product is ",n1 * n2)

#%%
GJ = [["Vadodara","manjalpur","Alkapuri"],["Ahemdabad","Vastrapur","Paldi"]]
def pl(s):
    lis = int(input("Enter the list number "))
    lisa = int(input("Enter the area number "))
    for s in lis:
        for lis in lisa:
            print(s[lis][0],s[lis][lisa])


#%%
NE= [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]

def pop(s):
    n = 0
    i = 0 
    sum_ = 0    
    for i in range(0,len(s)):
        sum_ = sum_ + s[i][1] 
        i = i + 1 
        n = n + 1 
    print("The sum is ",sum_)
    for i2 in s:
        i2 = len(s)
    print("The count is ",i2)
        



#%%          


verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def sentence():
    l = (verbs,nouns,adverbs,articles)
    for sen in l:
        article = random.choice(articles)
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        verb = random.choice(verbs)
        
        sen = article + " " + noun + " " + verb + " " + adverb
        sen = sen.capitalize()
        print(sen)
#%%

def sentence():
    l = str()
    for sen in range(5):
        article = random.choice(articles)
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        verb = random.choice(verbs)
        
        sen = article + " " + noun + " " + verb + " " + adverb
        sen = sen.capitalize()
        print(sen)


#%%
def add():
    add = 0
    while True:
        s = int(input("Enter the Name, enter 0 to quit "))
        if s == 0 :
            break
        add = add + s
    print(add)          



#%%

def l():
    lis = []
    while True:
        l = input("Name of List is enter quit to exit:")
        if l.lower() == "quit":
            break
        else:
            lis.append(l)
    print("Your list is",lis)



#%%

def r():
    r = random.seed(70)   

    print(r,random.randrange(30,35))
 
 

#%%
def s():
    a = 18+10+13+25+17+22+47+28
    print(a)
    print((a/1.75)/12)

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          

#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          

#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
#%%

#%%

#%%

#%%


#%%

#%%

#%%


#%%          
