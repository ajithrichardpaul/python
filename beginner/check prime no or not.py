a=int(input("enter the number="))
if a>1:
  for i in range (2,a):
    if(a%i)==0:
      print(a,"is not prime no")
      print(i,"times",a//i,"is",a)
      break
  else:
    print(a,"no is a prime no")
