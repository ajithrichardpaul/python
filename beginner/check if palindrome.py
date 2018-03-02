a=int(input("enter the number:"))
tem=a
rev=0
while(a>0):
  dig=a%10
  rev=rev*10+dig
  a=a//10
if(tem==rev):
  print("the given no is palindrome")
else:
  print("the given no is not palindrome")
