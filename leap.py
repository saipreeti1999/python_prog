a=int(input("enter a year:"))
if a%4==0 or a%400==0 and a%100!=0:
    print("it is leap year")
else:
    print("it is not a leap year")
