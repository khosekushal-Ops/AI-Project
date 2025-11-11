#this program is to demonstrate all datatype 
#string, list , tuples, sets, Dictonaries 

#First is string 
str1= 'This is single quoted string'
str2= "double quoted string"
str3= ''' tripple quoted string'''

print(f"length of {str1} is ",len(str1))

#indexing of string
print("this is for position index\t")
print(str1[1])
print(f"find lenth of string using len function like : \t",len(str1))
print(f"datatype of str1 is {type(str1)}")
print(f"datatype of str2 is {type(str2)}")
print(f"datatype of str3 is {type(str3)}")
print(f"print in reverse order {str1[-1]}")

print("\n\n")

welcome="This is the full length string"
print("out string is :=",welcome,"\n")

print("this will start from positon 1 till 5 and skip by 1=",welcome[0:7:1])
print(f"{welcome}:\t welcome[:4] ={welcome[:4]}")  
print(f"welcome[2:]={welcome[2:]}")
print(f"welcome[-4:-1]={welcome[-4:-1]}")
print(f"welcome[::-1]={welcome[::-1]}")
print(welcome[3])
print("upper=",welcome.upper())
print("lowwer:",welcome.lower())
print("capitalize:",welcome.capitalize())
print("swapcase:",welcome.swapcase())
print("title:",welcome.title())


