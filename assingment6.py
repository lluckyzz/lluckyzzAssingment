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
    lst.append("class")
    lst.pop(0)
    s1.add("class")
    d1.update({"class":"Sycob"})
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1)
      


ds(75,"lucky")
printds()
ds_update()







