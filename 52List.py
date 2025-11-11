numList =[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print([n for n in numList if n%2==0])

letters = ["apple","mange","orange"]
print(type(letters))

counter=0

for w in letters: 
    if 'a' in w.lower():
        counter=counter+1
print(f"a appear {counter} times ")        

print("-----------------------------------------------------------:")

list2=[12,54,34,65,76,87,45,45,4,5,6,7,87]

g = list2[0]
s = list2[0]

for n in list2:
    if n > g:
        g = n    
    if n < s:
        s = n             
print(f"largest:", g)
print("smallest:",s)
        
print('''----------------Create a list of square numbers from 1–20,
 but only include numbers greater than 100.--------''')
 
for n in range(1,20):
    if n*n >100:
        print(n*n)

print("-----------------------------------------------------------")
print("Given a nested list, flatten it using a list comprehension.")

a= [12,23,34,45,56,67]
b= [21,32,43,54,65,76] 
c = a.extend(b)
print("a",a)
print("b",b)
print("c",c)        
         
        