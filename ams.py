a,b=map(int,input().split())
for num in range(a+1,b):
  order=len(str(num))
  temp=num
  sum=0
  while temp>0:
    rem=temp%10
    sum+=rem**order
    temp=temp//10
  if num==sum:
    print(num,end=" ")
  
  
