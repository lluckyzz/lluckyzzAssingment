# Name :-Lucky pal
# class CO-B
# Topic :
"""
1) Create a function with a default parameter "file" storing the file path
2) Open the "file" in append mode
3) Use writelines() method to add your roll number, name, and class
4) Use readines() method to print your data in the prompt

Note: Use try...except block with suitable exception class

"""

def fl(file="Information.txt"):
    f=open(file,"+at")
    f.writelines(["roll no : 75","\nName : Lucky","\nclass : Sycob"])
    f.seek(0)
    try:
        print(f.readlines())
    except(FileNotFoundError):
        print("the file not yet created...")
    except Exception :
        print(Exception)
fl()

# Output --->>> 
"""

['roll no : 75\n', 'Name : Lucky\n', 'class : Sycob']

"""