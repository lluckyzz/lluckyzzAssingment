# Name :-Lucky pal
# class CO-B
# Topic :
"""
1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)

2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor

3) Create a method known as display in both the classes, to display the values of a,b and c

4) While accessing the private member an exception should be raised and a personalized message should be displayed and the exception
should be handled properly so that the rest of the code can get executed

"""
from colorama import init, Fore, Back, Style
    
class luckyzz_Exception(Exception):
    
    def __init__(self,msg):
        super().__init__(msg);

class A:
    
    __a=None # Private
    _b=None  # Protected
    c=None   # Public
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def display(self):
        print("a =",self.a)
        print("b =",self.b)
        print("c =",self.c);

class B(A):

    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    
    def display(self):
        print("Printing by display() of 'B' class :-");

        try:
           if(self.a):
               raise luckyzz_Exception(Fore.RED+    """(Error) :
you cannot access variable 'a' in B class because is Private member cannot be access.......!!!!!!!!"""+Fore.WHITE)
           
        except luckyzz_Exception as w:
           print(str(w));
        
        print("b =",self.b)
        print("c =",self.c)
        print()
        print("Printing by display() of 'A' class :-");
        super().display();
        
x=(input("Enter your name : "))
y=int(input("Enter your Roll no : "))
z=(input("Enter your class : "))

b=B(x,y,z);
b.display();

# Output ------------->>>
"""Enter your name : lucky
Enter your Roll no : 75
Enter your class : SYCOB
Printing by display() of 'B' class :-
(Error) :
you cannot access variable 'a' in B class because is Private member cannot be access.......!!!!!!!!
b = 75
c = SYCOB

Printing by display() of 'A' class :-
a = lucky
b = 75
c = SYCOB"""
            