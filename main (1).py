#1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

year=int(input("Input the Year: "))               #input year 
if(year%4==0):                                    #check whether year is divisible by 4 or not
    if(year%400==0):                              #if year is divisible by 400 
        print("Entered Year is a Leap Year.")     
    elif(year%100==0 and year%400!=0):
        print("It is not a Leap Year.") #if divisible by 100 but not 400
    else:
        print("Entered Year is a Leap Year.")
else:
    print("Entered Year is not a Leap Year.")
  