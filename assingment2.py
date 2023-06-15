
i=True
while i == True:

 print(" 1. addtion \n 2. subtraction \n 3. multiplication \n 4. dividion \n 5. floordividion \n 6. exponentiation \n 7.exit()")

 ari = int(input("choose the option to select : " ))

 if ari == 1:
     a = float(input("Enter the first number : "))
     b = float(input("Enter the second number : "))
     print("Addition is :",int(a+b),"\n")
 elif ari == 2:
     a = float(input("Enter the first number : "))
     b = float(input("Enter the second number : "))
     print("subtration is :",int(a-b),"\n")
 elif ari == 3:
     a = float(input("Enter the first number : "))
     b = float(input("Enter the second number : "))
     print("Multiplication is :",int(a*b),"\n")
 elif ari == 4:
     a = float(input("Enter the first number : "))
     b = float(input("Enter the second number : "))
     print("Division is :",int(a/b),"\n")
 elif ari == 5:
     a = float(input("Enter the first number : "))
     b = float(input("Enter the second number : "))
     print("floorDivision is :",int(a//b),"\n")
 elif ari == 6:
      a = float(input("Enter the first number : "))
      b = float(input("Enter the second number : "))
      print("Exponentiation is :",int(a**b),"\n")
 elif ari == 7:
    print("code exitted")
    i = False
 else:
    print("invalid option")


# Output****


"""1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 1
Enter the first number : 12
Enter the second number : 13
Addition is : 25
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 2
Enter the first number : 30    
Enter the second number : 20
subtration is : 10
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 3
Enter the first number : 12
Enter the second number : 13
Multiplication is : 156
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 4
Enter the first number : 4
Enter the second number : 2
Division is : 2
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 5
Enter the first number : 20
Enter the second number : 10
floorDivision is : 2
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 6
Enter the first number : 2
Enter the second number : 4
Exponentiation is : 16
 1. addtion 
 2. subtraction 
 3. multiplication 
 4. dividion 
 5. floordividion 
 6. exponentiation 
 7.exit()
choose the option to select : 7
code exitted"""