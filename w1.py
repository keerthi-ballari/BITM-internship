n=int(input())
if (n%2!=0):
    print("wierd")
elif(n%2==0 and n>=2 and n<=5):
    print("not wierd")
elif(n%2==0 and n>=6 and n<=20):
    print("wierd")
elif(n%2==0 and n>20):
    print("not wierd")
