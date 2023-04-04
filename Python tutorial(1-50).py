#COMMENT 

# print("Vishv  VISHV") 
# print(5 + 6)
# print(8*8)
# print(90-60)
# print(88-8)

# print(" Hii I am \"Vishv\" and \n I am a Good boy.")        #\n is used for a new line in Python.\" is used double coat a word in Line.
#                                                             #crtl + / is used to Comment/Uncomment code in Python
#                                                             # ''' -----''' is used to commentout a paragraph.




#DATA TYPES

# a = 4          #Integer 
# b = "Vishv"    #String
# c = 1.1        #Float 
# d = True       #Boolean
# print("The type of a is" , type(a))
# print("The type of c is" , type(b))
# print("The type of b is" , type(c))
# print("The type of d is" , type(d))



#ARITHEMATIC OPREATORS(+,-,*,/,**,//)

# a = 16                                          # "ALT + SHIFT + DOWNKEY" replicates a Line downward   
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)     #gives result of b times a
# print(a/b)      #gives result with decimal point
# print(a//b)     #gives result without decimal point
# print(a%b)      #gives result without decimal point


#TAKE USER INPUT

# a = input()                                           #input() is used to take input from user
# print("My name is",a)

# x = int(input("Enter a number: "))                    #int(input()) is because Python shouldn't consider the value as a string.
# y = int(input("Enter the second number: "))           #It will consider and allow user to print integer in program.
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)


#STRING

# name = "Vishv !!!"                                    #'''-------''' allows you to print a para with changing line without using \n. 
# friend = "RAHUL"                                    #It is known as Multiline string. 
# apple =''''He said,                                          
#            I am okay with playing football.
#            It will be fine for me.'''
# print(apple)
# print("Hello " + name)
# print(name[0])                                      #[0] gives Index of VISHV which means gives first alphabet of VISHV.
# print(friend[3])
# for character in apple:
#     print(character)                             #Using for loop we can lop through strings.        
# print(len(name))                                   #len funtion is used to print length of a string.
# print(name[0:5])
# print(name[0:-3])
# print(name.upper())                                #upper() converts string to uppercase/capital.
# print(name.lower())                                #lower() converts string to lowercase/small.
# print(name.rstrip("!"))                            #rstrip() removes an alphabet from the string.
# print(name.replace("!!!"," NAGDE"))                #replace() replaces string.
# print(name.split())                                #split() makes list of words in string on basis of space.
# a = "introduction tO PYthon"
# print(a.capitalize())                              #capitalize() converts first letter of string in capital.
# print(a.center(50))                                #center() adds no. of spacesbefore a string.
# print(a.count("o"))                                #count() displays no. of times a alphabet exists in a string.
# print(name.endswith("!!!"))                        #endswith() says if a string ends with particular alphabets.
# print(a.find("tO"))                                #find() gives index of particular word in a string.
# # print(a.index("to"))                             #index() gives erroe if a word isn't in a string.
# print(a.islower())                                 #islower() checks all character in string are in lowercase.
# print(a.swapcase())                                #swapcase() converts upper-lower , lower-upper.
# print(a.title())                                   #title() First letter of each character in a string gets capitalized.



#IF-ELSE STATEMENT

# a = int(input("Enter your age: "))
# print("Your age is " , a)
# if(a>=18):                                                  #Conditional opreators( > , < , >= , <= , == , != )
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")

# budget = int(input("Enter the amount :"))
# appleproduct = 210
# if(budget >= appleproduct):
#     print("You can afford it.")
# elif(budget>180<appleproduct):
#     print("You can afford if you add some more money to it.")
# elif(budget<50):
#     print("You need to work hard and add much more money to afford it.")
# else:
#     print("You can't afford it")




#MATCH STATEMENT 

# x = int(input("Enter the value: "))
# match x:
#     case 0:
#         print("The value of x is o")
#     case 4:
#         print("The value of x is 4")
#     case _:
#         print(x)




#FOR LOOP

# name = "Abhishek"
# for i in name: 
#     print(i)

# colors =["Red","Green","Blue","Black"]
# for color in colors:                                    #if 'color' used here then for printing also u should use 'color'. 
#     print(color)

# for i in colors:                                        #if 'i' used here then for peinting also use 'i'.
#     print(i)

# for k in range(20):                                     #range() is used to print integers till a limit.
#     print(k)
#     # print(k+1)

# for k in range(1,8):                                    #range(_,_) used to print from one integer to other.
#     print(k)

# for i in range(1,10,2):                                    #range(_,_,_) skips 2 integers from 1-1o      
#     print(i)





#WHILE LOOP

# i = 0
# while (i<=3):
#     print(i)
#     i = i+1

# i = int(input("Enter the number : "))
# while (i<=38):
#     i = int(input("Enter the number : "))             #Run this code on online compiler.In VSD it's not running.
#     print(i)
# print("Done with the loop.")

# count = 5
# while(count > 0):
#     print(count)
#     count = count - 1
# else:
#     print("I am inside else. ")




#BREAK AND CONTINUE STATEMENT

# for i in range(15):                                          #Run this on online compiler.Your VSD isn't running this code.
#     if( i == 10):                                            #This allows code to run only till 10 integers.        
#         break                                                #This breaks the integers and don't dislapy when it goes above 10.
#     print("5" , "x" , i+1 , "=" , 5*i+1 )                    #'break' stops the Iteration.
# print("After 10 Table will vanish as 'break' is used")


# for i in range(15):                                          #Run this on online compiler.Your VSD isn't running this code.                                          
#     if( i == 10):
#         print("Here continue statement is used.")
#         continue                                             #'continue' skips the Iteration.
#     elif(i == 5):
#         print("Here continue statement is used")
#         continue                                             #'continue' skips the Iteration.      
#     print( "5" , "x" , i+1 , "=" , 5*i+1 )




#PYTHON FUNCTIONS(def)

# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isGreater(a,b):
#     if(a>b):
#         print("a is greater than b.")
#     else:
#         print("b is greater than a.") 
# def isLesser(a,b):
#     pass                                                #pass skips the code and error and code can be completed later.
# a = int(input("Enter your number : "))
# b = int(input("Enter your number : "))
# calculateGmean(a,b)





#LIST IN PYTHON

# marks = [ 3 , 5 , 6 , "Vishv" , True ]
#           0 , 1 , 2 ,   3     ,   4                  #Positive Indexing     
#          -5 ,-4 ,-3 ,  -2     ,   -1                 #Negative Indexing  
          
# print(marks)                                         #Lists can be changes,Tuples can't be changed.
# print(type(marks))                                 #We can also add strings in a list of Integers.
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-5])
# print(marks[-4])
# print(marks[-3])
# print(marks[-2])
# print(marks[-1])

# if 6 in marks:
#     print("Yes it is present.")
# else:                                               #Used to check if a element is presemt in List or not.    
#     print("No it's not present.")

# if "shv" in "Vishv":
#     print(True)
# else:                                               #Used to check if particular alphabets are present in a String or not.
#     print(False)
# print(marks[2:4])                                   #Used to print from a particular Index.

# lst = [i for i in range(10)]                           #List Comphrehension      
# print(lst)
# lst = [i*i for i in range(10) if i%2==0] 
# print(lst)





#LIST METHODS

# l = [13,17,1,9,3,5,9,7,9]
# print(l)
# l.append(10)                                #append() adds a element to the list.
# l.sort()                                    #sort() sorts elements in list according to ascending order.
# l.sort(reverse=True)                        #sort(reverse=True) sorts elements in list according to descending order.
# l.reverse()                                 #reverse() reverses given list.
# print(l.index(5))                           #index() displays value of particular element is list.
# print(l.count(9))                           #count() counts number of time a element is displayed in a list.
# m=l.copy()                                  #copy() copies the list as it is.
# m[0]=0
# print(l.insert(2,455))                      #insert(index,element)used to insert element on particular index.
# print(l.insert(1,745))                      #insert(index,element)used to insert element on particular index.
# m=[55,56,57]
# # l.extend(m)                               #extend() is used to open old list and add new list at its end.Used for joining two lists.
# k = l+m                                     #This is also usedto join two lists.
# print(l)





#TUPLE(SAME AS LIST JUST CAN'T BE CHANGED)

# tup = (1,)                                     #If Tuple consists of single elememt then you should give a comma(,) after it.
# print(type(tup),tup)
# tup = (1,5,6,"Green",True)                     #In Tuples () brackets are used rather than []. 
# print(type(tup),tup)
# print(len(tup))                                #len() used to print length of Tuple.
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])                                  #Tuple has same +ve and -ve indexing as in Lists.
# print(tup[-1])
# print(tup[-2])
# print(tup[-3])
# print(tup[-4])
# print(tup[-5])    
# if "Green" in tup:                             #Used to check whether a element is present in Tuple.
#     print("It is present in Tuple.")
# tup2 = tup[1:4]
# print(tup2)                                    #Has same functions/methods as of List.




#f-STRINGS 

# letter = "Hey my name is {} and I am from {}."
# name ="Vishv"
# country ="India"
# print(letter.format(name,country))                                                                   #This was the old method used.
# print(f"Hey my name is {name} and I am from {country}.")
# print(f"WE use f-Strings like this:Hey my name is {{name}} and I am from {{country}}.")              #f"---" F string is used now.




#DOC-STRINGS

# def square(n):
#     '''Takes in a number n,returns the square of number n.'''                #This is a DOC,not a comment.
#     print(n**2)                                                              #DOC string is to be written after class,before body of code.
# square(5)
# print(square.__doc__)                                                        #This is a DOC function used to display DOC string.




#RECUSION IN PYTHON

# n = int(input("Enter the Number : "))
# def factorial(n):
#     if(n==0 or n==1):
#         return 1 
#     else:
#         return n * factorial(n-1)
# print(factorial(n))
# print(factorial(4))
# print(factorial(5))




#SETS IN PYTHON

# s = {2,4,2,6,"Vishv",False}                       #Sets are unordered collection of data items.So it don't have fixed index.
# print(s)                                          #Set don't take repeated values as compared to list.

# for value in s:                                   #To access value in set use for loop.
#     print(value)

# Vishv = set()                                     #Empty Set is made like this.
# print(type(Vishv)) 

# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))                               #union() combines elements of two sets.
# s1.update(s2)                                     #update() adds/updates values of s2 in s1.
# print(s1,s2)        

# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.union(cities2)                    #union() combines elements of two sets.
# cities3 = cities.intersection(cities2)             #intersection() combines same element of two sets.
# print(cities3)      
# cities.intersection_update(cities2)                #intersection_update() updates a set with intersection of two sets.
# print(cities)
# cities3 = cities.symmetric_difference(cities2)     #symmetric_difference() gives symmetric difference between two sets.Don't show similar items of two sets.
# print(cities3)
# cities3 = cities.difference(cities2)               #difference() prints items present only in orignal set and not in both sets.
# print(cities3)                         
# print(cities.isdisjoint(cities2))                  #isdisjoint() checks whether items in a set are present in othe set or not.

# a = {1,2,3,4,5,6,7,8,9,10}
# b = {1,3,5,7,9}
# c = {2,4,6,8,10}
# print(a.issuperset(b))                              #issuperset() checks whether a set is superset/not.
# print(b.issubset(a))                                #issubset() checks whether a set is superset/not.
# b.add(8)                                            #add() adds single item to a set.
# b.update(c)                                         #update() updates a set with values of other set.
# b.remove(1)                                         #remove() removes a element from set.Shows error if item not present in set.
# b.discard(2)                                        #discard() removes a element in set.Don't show error if item not present in set.
# item = b.pop()                                      #pop() shows and pops a random value from a set.
# print(b)
# print(item)
# del a                                               #del() deletes a entire set. 
# print(a)
# a.clear()                                           #clear() deletes all items of a set.
# print(a)

# if 1 in a:                                  
#     print("1 is present in set.")                   #used to check item present in set or not.                    
# else:
#     print("1 is not in the set.")



#DICTIONARY IN PYTHON

# dic = {
#     38:"Vishv",                                               #(38,39,40,41) are key and(Vishv,Rohit,....) are its values.
#     39:"Rohit",
#     40:"Kaustubh",
#     41:"Abhishek"
# }
# print(dic[40]) 

# info = {'name':"Vishv" , 'age':19 , 'branch':"AIML"}
# print(info)
# print(info['name'])
# print(info['name2'])                                            #error occurs due to name2 doesn't exist.
# print(info.get('name2'))                                        #error doesn't occur even if name 2 doesn't exist.
# print(info.keys())                                              #gives keys in the dictionary.
# print(info.values())                                            #gives values in the dictionary.  
# print(info.items())                                             #gives key,values in pair.

# ep1 = {122:"Harry" , 236:"Vishv" , 123:"Rohit"}
# ep2 = {121:"Ravi" , 235:"Om" , 260:"Vijay"}
# ep1.update(ep2)                                                 #update() updates and add new elements in dictionary.
# ep1.clear()                                                     #clear() clears all records in dictionary.
# ep1.pop(122)                                                    #pop() deletes particular key,value from dictionary.
# ep1.popitem()                                                   #popitem() deletes the last key,value(record) in dictionary.
# del ep1[122]                                                    #del deletes a record from dictionary.
# print(ep1)





#EXCEPTION HANDLING

# a = input("Enter the number : ")
# print(f"Multiplication of {a} is : ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} * {i} = {int(a)*i}")
# except Exception as e:                                           #except doesn't show erroe instead it will print e.
#     print("Sorry some erroe occured.")

# print("Some imp lines of code")
# print("End of program")




#FINALLY KEYWORD IN PYTHON

# try:
#     l =[1,5,6,7]
#     i = int(input("Enter the index : "))
#     print(l[i])
# except:
#     print("Someerror occured")
# finally:                                                          #Finally is used wheteher error occurs or not.
#     print("I am always executed")




# RAISING CUSTOM ERRORS

# a = int(input("Enter a number between 5 and 9: "))
# if(a<5 or a>9):
    # raise ValueError("Try number between 5 and 9")                  #raise used to raise error in program.
#VIDEO 39 (SECRET CODE) QUESTION




#IF-ELSE METHOD SHORT HAND METHOD

# a = 370
# b = 260
# print("A") if a<b else print("=") if a==b else print("B")
# c = 9 if a>b else 0
# print(c)



#ENUMARATE FUNCTION

# marks = [12 , 38 , 42 , 55 , 68]

# index = 0
# for marks in marks:
#     print(marks)                                        #This is a bit difficult way so ennumerate function is used.
#     if(index == 4):
#         print("Awesome Marks")
#     index += 1

# for index, mark in enumerate (marks , start=1):         #start=1 starts the index from 1 instead of 0.
    # print(mark)
    # if(index == 3):
        # print("Awesome Marks")



#IMPORTING IN PYTHON

# import math
# result = math.sqrt(9)
# print(result)       

# from math import sqrt , pi
# result = sqrt(9)*pi                                   #from keyword
# print(result)

# from math import sqrt as s, pi
# result = s(9)*pi                                      #as keyword   
# print(result)

# import math
# print(dir(math))                                      #dir keyword 
# print(math.sin , type(math.sin))




#FILE INPUT UOTPUT IN PYTHON

# f = open('myfile.txt', 'r')                             #myfile.txt be another file.(r = read mode),(w = write mode)
# text = f.read()                                         #f.read will print/read text in myfile file.
# print(text)                                             #'r' mode is default mode.
# f.close()                                               #F.close() is used to close the file you opened.

