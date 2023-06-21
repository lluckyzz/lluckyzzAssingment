# Name :-Lucky pal
# class CO-B
# Topic :
"""
1)Create a function named ds with parameters roll_no and name.
2)Add those parameters in the following data structures:
list, tuple, sets and dictionaries
3) After adding values
change the values during runtime
4)Delete these data structures

"""
# defining a method
def ds(roll_no,name):
    global lst 
    global t1
    global s1
    global d1
    lst=[roll_no,name]
    t1=(roll_no,name)
    s1={roll_no,name}
    d1={"Roll no ": roll_no , "Name ":name}


def printds():
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1,"\n")


def ds_update():
    print("____________________________________________________________\n")
    print("Updating the data structures ...")
    print("____________________________________________________________\n")
    x=int(input("Enter the roll no : "))
    y=input("Enter the name : ")
    ds(x,y)
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1)

def applyingmeth():
    print("____________________________________________________________\n")
    print("Applying some method in data structures ...")
    print("____________________________________________________________\n")
    lst.append("class")
    print("\n--> appending the List : ",lst)
    lst.pop(0)
    print("--> poping at [0] form the List : ",lst,"\n")

    s1.add("class")
    s1.add("Sycob")
    print("\n--> adding item into Set : ",s1)
    s1.pop()
    print("--> poping the item from Set : ",s1,"\n")

    d1.update({"class":"Sycob"})
    print("\n--> adding the item in Dictionary : ",d1)
    d1.pop("class")
    print("--> poping the item from dictionary : ",d1)

def deletemeth():
    print("____________________________________________________________\n")
    print("Calling the data structures after deleting  ...")
    print("____________________________________________________________\n")
    del lst
    del t1
    del s1
    del d1
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1)  

ds(75,"lucky")
printds()
ds_update()
applyingmeth()
deletemeth()



#----->>>> Output 
"""
List :  [75, 'lucky'] 

Tuple :  (75, 'lucky') 

Set :  {75, 'lucky'} 

Dictionary :  {'Roll no ': 75, 'Name ': 'lucky'} 

____________________________________________________________

Updating the data structures ...
____________________________________________________________

Enter the roll no : 98
Enter the name : maaz

List :  [98, 'maaz'] 

Tuple :  (98, 'maaz') 

Set :  {'maaz', 98} 

Dictionary :  {'Roll no ': 98, 'Name ': 'maaz'}
____________________________________________________________

Applying some method in data structures ...
____________________________________________________________


--> appending the List :  [98, 'maaz', 'class']
--> poping at [0] form the List :  ['maaz', 'class'] 


--> adding item into Set :  {'maaz', 98, 'class', 'Sycob'}
--> poping the item from Set :  {98, 'class', 'Sycob'} 


--> adding the item in Dictionary :  {'Roll no ': 98, 'Name ': 'maaz', 'class': 'Sycob'}
--> poping the item from dictionary :  {'Roll no ': 98, 'Name ': 'maaz'}
____________________________________________________________

Calling the data structures after deleting  ...
____________________________________________________________
--->>>List

Traceback (most recent call last):
  File "/home/raj/python/python assingment/assingment6.py", line 81, in <module>
    deletemeth()
  File "/home/raj/python/python assingment/assingment6.py", line 68, in deletemeth
    del lst
UnboundLocalError: local variable 'lst' referenced before assignment


-->>>Tuple

Traceback (most recent call last):
  File "/home/raj/python/python assingment/assingment6.py", line 81, in <module>
    deletemeth()
  File "/home/raj/python/python assingment/assingment6.py", line 69, in deletemeth
    del t1
UnboundLocalError: local variable 't1' referenced before assignment


-->>>Set

Traceback (most recent call last):
  File "/home/raj/python/python assingment/assingment6.py", line 81, in <module>
    deletemeth()
  File "/home/raj/python/python assingment/assingment6.py", line 70, in deletemeth
    del s1
UnboundLocalError: local variable 's1' referenced before assignment


-->>>Dictionary

Traceback (most recent call last):
  File "/home/raj/python/python assingment/assingment6.py", line 81, in <module>
    deletemeth()
  File "/home/raj/python/python assingment/assingment6.py", line 71, in deletemeth
    del d1
UnboundLocalError: local variable 'd1' referenced before assignment



"""








