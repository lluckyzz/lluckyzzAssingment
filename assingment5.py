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
print(" _____________________________________________________")
print("|________________________sum()________________________|")

print(" Sum of all elements is : ",sum(lst1))
print("______________________________________________________\n\n")




print(" _____________________________________________________")
print("|_______________________min()_________________________|")
print(" Smallest value in list : ",min(lst1))
print("______________________________________________________\n\n")




print(" _____________________________________________________")
print("|________________________max()________________________|")
print(" largest value in list : ",max(lst1))
print("______________________________________________________\n\n")




print(" _____________________________________________________")
print("|_________________sort()in ascending__________________|")
print("Before sorting a list : ",lst1)
lst1.sort()
print("After sorting in acending order : ",lst1)
print("______________________________________________________\n\n")




print(" _____________________________________________________")
print("|________________sort()in descending__________________|")
lst1.sort(reverse=True)
print("After sorting in Decending order : ",lst1)
print("______________________________________________________\n\n")




print(" ____________________________________________________")
print("|__________converting the list into tuple____________|")
t1=tuple(lst1)
print("list : ",lst1)
print("tuple: ",t1)
print("______________________________________________________\n\n")





print("_____________________________________________________")
print("|________________________del_________________________|")

del lst1
# print(lst1)#------------->>>>> throws - NameError: name 'lst1' is not defined


print("If we are trying to print after deleting the list \nthen it throws - NameError: name 'lst1' is not defined")
print("______________________________________________________\n\n")



# Output -------->>>
"""
Enter the length of list : 5
Enter the no at index  0 :  1
Enter the no at index  1 :  2
Enter the no at index  2 :  3
Enter the no at index  3 :  4
Enter the no at index  4 :  5
 _____________________________________________________
|________________________sum()________________________|
 Sum of all elements is :  15
______________________________________________________


 _____________________________________________________
|_______________________min()_________________________|
 Smallest value in list :  1
______________________________________________________


 _____________________________________________________
|________________________max()________________________|
 largest value in list :  5
______________________________________________________


 _____________________________________________________
|_________________sort()in ascending__________________|
Before sorting a list :  [1, 2, 3, 4, 5]
After sorting in acending order :  [1, 2, 3, 4, 5]
______________________________________________________


 _____________________________________________________
|________________sort()in descending__________________|
After sorting in Decending order :  [5, 4, 3, 2, 1]
______________________________________________________


 ____________________________________________________
|__________converting the list into tuple____________|
list :  [5, 4, 3, 2, 1]
tuple:  (5, 4, 3, 2, 1)
______________________________________________________


_____________________________________________________
|________________________del_________________________|
If we are trying to print after deleting the list 
then it throws - NameError: name 'lst1' is not defined
______________________________________________________

"""
