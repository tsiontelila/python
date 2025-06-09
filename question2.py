name=(input("what is your name:"))
print (name)
subject1=int(input("enter your result:"))
subject2=int(input("enter you result:"))
subject3=int(input("enter you result:"))
subject4=int(input("enter you result:"))
subject5=int(input("enter you result:"))
average=(subject1+subject2+subject3+subject4+subject5) /5
if average>= 90:
    print("A")
elif average>=80:
    print("B")
elif average>=79:
    print("C")
elif average>=60:
    print("D")
else:
    print("F")


