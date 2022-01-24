print ("hello python world!")

message = "hello python crash course world!"
print(message)

message = "hello  python crash course reader "
print(message)

name = "sushma"
print(name.title())


name = "Adva Nce"
print(name.upper())
print(name.lower())

first_name = "adva"
last_name = "nce"
full_name = first_name + " " + last_name
print(full_name)

print("\tpython" )

print("languages:\npython\njava\nc\nphp")

print("languages:\n\tpython\n\tjava\n\tc\n\tphp")

age= 22
message = " Happy "  +   str(age) +  "nd birthday!"
print(message)

a = 10
b = 20
sum = a + b
print(sum)

# saurab is a good boy.
print("hello saurabh!")

things = ['hat', 'doll', 'bat', 'table']
print(things)

things = ['hat', 'doll', 'bat', 'table']
print(things[0].title())


things = ['hat', 'doll', 'bat', 'table']
print(things[1])
print(things[3])
print(things[2])


things = ['hat', 'doll', 'bat', 'table']
print(things[-1])




things = ['hat', 'doll', 'bat', 'table']
message = "my first things " + things[0].title() + "."
print(message)


things = ['hat', 'doll', 'bat', 'table']
print(things)

things[0] = "jug"
print(things)



things = ['hat', 'doll', 'bat', 'table']
print(things)

things.append('jug')
print(things)

things = ['hat', 'doll', 'bat', 'table']
print(things)

things.insert(0,'jug')
print(things)

things = ['hat', 'doll', 'bat', 'table']
print(things)

del things[0]
print(things)

things = ['hat', 'doll', 'bat', 'table']
print(things)

del things[1]
print(things)

things = ['hat', 'doll', 'bat', 'table']
print(things)
popped_thing = things.pop()
print(things)
print(popped_thing)

things = ['hat', 'doll', 'bat'] 
last_owned = things.pop()
print("The last thing I owned was a " + last_owned.title() + ".")

cars = ['toyota', 'suzuki', 'audi', 'honda']
cars.sort()
print(cars)

cars = ['toyota', 'suzuki', 'audi', 'honda']
cars.sort(reverse=True)
print(cars)

cars = ['toyota', 'suzuki', 'audi', 'honda']
print(cars)
cars.reverse()
print(cars)



name="sujata"
print(name)

x=1+2*3-8/4
print(x)

x=int(98.6)
print(x)

print("123" + "abc") 

name = "Hello Sarah "
print(name)

Howdy = "Hello Sarah "
print(Howdy)

a = 96
b = 25
sum= (a + b)
print(sum)

#name = input("Please enter your name: ")
#print("Hello " + name + "")


#hrs = input("Enter Hour:")
#rate = input("Enter Rate per Hour:")
#pay = float(hrs)*float(rate)
#print("pay:",pay)

#name = input("Enter your name")
#print ("Hello", name)

if x == 5 :
 print('is 5')
 #print('is still 5')
 #print('third 5')

x = 0
if x < 2 :
 print('Small')
elif x < 10 :
 print('Medium')
else :
 print('LARGE')
 print('All done') 

if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('two or more')
else :
    print('something else')



sh= input ("Enter Hours: ")
sr= input ("Enter Rate: ")
fh= float(sh)
fr= float(sr)
#print(fh,fr)
if fh>40 :
    #print("Overtime")
    reg= fr*fh
    otp=(fh-40.0)*(fr*0.5)
    #print("reg,opt")
    xp= reg + otp
else:
    #print("Regular")
    xp=fh*fr
print(xp)


try:
    s = raw_input("please input your score:")
    score = float(s)
    if score > 1.0:
        print( "value out of range")
    elif 1.0 >= score>=.9:
        print( "A")
    elif .9 > score>=.8:
        print( "B")
    elif .8 >score>=.7:
        print ("D")    
    elif .7 >score>=.6:
        print ("D")
except:
    print ("Error , please input is numeric")



def thing():
    print('Hello')
    
print('There')    

def addtwo(a,b):
    added = a + b
    return a
x = addtwo(2,7)
print(x)


def func(x):
    print(x)
func(10)
func(20)

def computepay(hours,rate):
    #print("In computepay",hours,rate)
  if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0)*(rate*0.5)
        pay = reg + otp
  else:
        pay = hours + rate
        #print("Returning", pay)
  return pay      

sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)
xp = computepay(fh,fr)
print("Pay",xp)


import sys
score = input("Enter Score: ")
try :
    score = float(score)
    if score > 1.0:
        print("Bad score")
        #print letter grade
    elif 1.0 >=score>=.9:
        print("Grade is A" + str(score))
    elif .9 >score>=.8:
        print("B")
    elif .8 >score>=.7:
        print("C")
    elif .7 >score>=.6:
        print("D")
    elif .6 >score>=.5:
        print("F")
except valueError :
    print("You need to input a number ")


largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" :
        break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest=num
    elif num < smallest :
        smallest=num
    elif largest is None:
        largest=num
    elif num > largest :
       largest=num
print("Maximum is", int(largest))
print("Minimum is", int(smallest))




























