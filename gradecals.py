sub1 =int(input("enter marks of subject1:"))
sub2 =int(input("enter marks of subject2:"))
sub3 =int(input("enter marks of subject3:"))
sub4 =int(input("enter marks of subject4:"))
sub5 =int(input("enter marks of subject5:"))

total=sub1 +sub2+sub3+sub4+sub5

percentage = total/5

print("percentage=",percentage)

if sub1<35 or sub2<35 or sub3<35 or sub4<35 or sub5<35:
    print("failed in subject")
else:
    if percentage>=75:
        print("distinction")
    elif percentage>=60:
        print("first class")
    elif percentage>=50:
        print("second class")
    elif percentage>=35:
        print("pass")
    else:
        print("fail")
