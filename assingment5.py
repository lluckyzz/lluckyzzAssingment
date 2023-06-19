#  Name : Lucky pal
# class : CO-B 
# roll no : 75
# Topic :
'''Take input from the user of 5 numbers and store it in a list.
Perform below operations:
1) Calculate the sum of all the elements in the list
2) Find the smallest number
3) Find the largest number
4) Display list in ascending order
5) Display list in descending order
6) Convert list into tuple
7) Delete the list'''

lst1=[]
k=-1
num=int(input("Enter the length of list : "))
for i in range(num):
  k+=1
  print("Enter the no at index ",k,": ",end=" ")
  n=int(input())
  lst1.append(n)
print("_____________________________________________________")
print("********************    sum()    ********************")
print("_____________________________________________________")
print("Sum of all elements is : ",sum(lst1),"\n")

print("_____________________________________________________")
print("********************    min()    ********************")
print("_____________________________________________________")
print("Smallest value in list : ",min(lst1),"\n")

print("_____________________________________________________")
print("********************    max()    ********************")
print("_____________________________________________________")
print("largest value in list : ",max(lst1),"\n")

print("_____________________________________________________")
print("**************** sort()in ascending *****************")
print("_____________________________________________________")
print("Before sorting a list : ",lst1,"\n")
lst1.sort()
print("After sorting in acending order : ",lst1)

print("_____________________________________________________")
print("**************** sort()in descending ****************")
print("_____________________________________________________")
lst1.sort(reverse=True)
print("After sorting in Decending order : ",lst1,"\n")

print("_____________________________________________________")
print("********** converting the list into tuple ***********")
print("_____________________________________________________")
t1=tuple(lst1)
print("list : ",lst1)
print("tuple: ",t1,"\n")

print("_____________________________________________________")
print("********************     del     ********************")
print("_____________________________________________________")
del lst1
print(lst1)#------------->>>>> throws - NameError: name 'lst1' is not defined


# Output -------->>>
"""
Enter the length of list : 5
Enter the no at index  0 :  1
Enter the no at index  1 :  223
Enter the no at index  2 :  12
Enter the no at index  3 :  34
Enter the no at index  4 :  1
_____________________________________________________
********************    sum()    ********************
_____________________________________________________
Sum of all elements is :  271 

_____________________________________________________
********************    min()    ********************
_____________________________________________________
Smallest value in list :  1 

_____________________________________________________
********************    max()    ********************
_____________________________________________________
largest value in list :  223 

_____________________________________________________
**************** sort()in ascending *****************
_____________________________________________________
Before sorting a list :  [1, 223, 12, 34, 1] 

After sorting in acending order :  [1, 1, 12, 34, 223]
_____________________________________________________
**************** sort()in descending ****************
_____________________________________________________
After sorting in Decending order :  [223, 34, 12, 1, 1] 

_____________________________________________________
********** converting the list into tuple ***********
_____________________________________________________
list :  [223, 34, 12, 1, 1]
tuple:  (223, 34, 12, 1, 1) 

_____________________________________________________
********************     del     ********************
_____________________________________________________
Traceback (most recent call last):
  File "/home/raj/python/python assingment/assingment5.py", line 62, in <module>
    print(lst1)
NameError: name 'lst1' is not defined

"""
