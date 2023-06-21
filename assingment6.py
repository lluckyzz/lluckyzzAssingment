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
def ds(roll="no ", name="argument passed"):
    return roll,name


print("-->> Taking info ")
x=int(input("Enter the roll no : "))
y=input("Enter the name no : ")

print("\n\n-->> putting the value in list")
lst1=[ds(x,y)]
print(lst1,"\n\n")

print("-->> putting the value in tuple")
t1=(ds(x,y))
print(t1,"\n\n")

print("-->> putting the value in set")
s1=set({ds(x,y)})
print(s1)

print("\n\n-->> putting the value in dictionary")

d1={
    "rollno":x,
    "name":y
    }

