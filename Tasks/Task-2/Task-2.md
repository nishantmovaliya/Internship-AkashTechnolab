<b>Comments</b>


```python
#this is a comment
#print Hello World
print('Hello World!!!')

'''This is a 
    example of 
    multi-line comment
'''

"""This is a 
    example of 
    multi-line comment
"""
```

<hr style="border:1px solid black"><b>Variables</b>


```python
#How to Declare and use a Variable
a=10
b=10.5
c="Nishant"

print(a)
print('Value of b:',b)
print('My name is ',c)

#Assigning multiple values to multiple variables
print()
a,b,c= 10,10.5,"Nishant"
print('a:',a,'b:',b,' My name is',c)

#Assign the same value to multiple variables
print()
a=b=c=5
print("a:",a,"b:",b,"c:",c)

```

    10
    Value of b: 10.5
    My name is  Nishant
    
    a: 10 b: 10.5  My name is Nishant
    
    a: 5 b: 5 c: 5
    

<hr style="border:1px solid black"><b>Number Datatype</b>


```python
n1 = 10

print (n1, "is of type", type (n1))

n2 = 10.5

print (n2, "is of type", type (n2)) 
print (n2, "is complex number?", isinstance (10.5, int))

n3 = 1+ 2j

print (n3, "is complex number?", isinstance (1 + 2j, complex))
```

    10 is of type <class 'int'>
    10.5 is of type <class 'float'>
    10.5 is complex number? False
    (1+2j) is complex number? True
    

<hr style="border:1px solid black"><b>String Datatype</b>


```python
name = "Nishant Movaliya"

# Prints complete string 
print ("Name is : ", name)

# Prints first character of the string

print (name [0])

# Prints characters starting from 3rd to 5th

print (name [2:5])

# Prints string starting from 3rd character 
print (name [2:])

# Prints string two times 
print (name * 2)

# Prints concatenated string

print (name + "Hello")
```

    Name is :  Nishant Movaliya
    N
    sha
    shant Movaliya
    Nishant MovaliyaNishant Movaliya
    Nishant MovaliyaHello
    

<hr style="border:1px solid black"><b>List Datatype</b>


```python
list1 = [15, 10.5, 'Nishant']

print (list1)
```

    [15, 10.5, 'Nishant']
    


```python
list1= [10, 20, 30, "Nishant", 40, 50, "Movaliya", 60]

# list1 [2] = 30

print ("list1 [2] = ", list1 [2])

# list1[0:3] = [10, 20, 35] 

print ("list1 [0:3] = ", list1 [0:3])

# list1[5:] = [50, 'Movaliya', 60]

print ("list1[5:] = ", list1 [5:])
```

    list1 [2] =  30
    list1 [0:3] =  [10, 20, 30]
    list1[5:] =  [50, 'Movaliya', 60]
    


```python
# creating an empty list

lst = []

# number of elements as input

n = int(input("Enter number of elements : "))

# iterating till the range

for i in range(0, n):
    ele = input ("Enter Value: ")
    lst.append(ele) # adding the element

print (lst)
```

    Enter number of elements : 5
    Enter Value: 12
    Enter Value: Nishant
    Enter Value: Movaliya
    Enter Value: 20.5
    Enter Value: Shyam
    ['12', 'Nishant', 'Movaliya', '20.5', 'Shyam']
    

<hr style="border:1px solid black"><b>Tuple Datatype</b>


```python
tuple1 = (10, 20, 30, "Nishant", 40, 50, "Movaliya", 60)

print (tuple1)
```

    (10, 20, 30, 'Nishant', 40, 50, 'Movaliya', 60)
    


```python
tuplel = (10, 20, 30, "Nishant", 40, 50, "Movaliya", 60)

#tuplel [2] = 30 
print ("tuplel [2]=", tuplel [2])

#tuplel (0:3] [10, 20, 35]

print ("tuplel [0:3]", tuplel [0:3])

#tuplel[5:] = [50, 'Movaliya', 60}

print ("tuplel [5:] = ", tuplel [5:])
```

    tuplel [2]= 30
    tuplel [0:3] (10, 20, 30)
    tuplel [5:] =  (50, 'Movaliya', 60)
    


```python
#creating an empty List

ls = []

#number of elements as input

n = int(input("Enter number of elements : "))

# iterating till the range

for i in range(0, n):
    ele = input("Enter Value: ")
    ls.append(ele) # adding the element
    
tupl=tuple (ls)

print(ls)

print(tupl) 
```

    Enter number of elements : 5
    Enter Value: 121
    Enter Value: 34.30
    Enter Value: Gopal
    Enter Value: Mohan
    Enter Value: 35
    ['121', '34.30', 'Gopal', 'Mohan', '35']
    ('121', '34.30', 'Gopal', 'Mohan', '35')
    

<hr style="border:1px solid black"><b>Dictionary Datatype</b>


```python
d = {1: 'Akash', 2: 'Technolabs', 'key': 10}

print (type (d))

print ("d[1] = ", d[1])

print ("d[2] = ", d[2])

print ("d['key'] = ", d['key'])
```

    <class 'dict'>
    d[1] =  Akash
    d[2] =  Technolabs
    d['key'] =  10
    


```python
mydict = {}

for totnum in range(0, int (input('Input the total number : '))): 
    a, b = input('Enter the key value pair :').split() 
    if a in mydict:
        mydict[a].append(b)
    else:
        mydict[a] = [b]

print(mydict)
```

    Input the total number : 5
    Enter the key value pair :1 Krishna
    Enter the key value pair :2 Gopal
    Enter the key value pair :3 Shyam
    Enter the key value pair :4 Mohan
    Enter the key value pair :5 Achyut
    {'1': ['Krishna'], '2': ['Gopal'], '3': ['Shyam'], '4': ['Mohan'], '5': ['Achyut']}
    


```python

```
