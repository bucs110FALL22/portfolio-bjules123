#Part A

#n = 101
count = 0
upper_limit = 20
iters={}
for n in range(2, upper_limit, 1):
 while n>1:
  count = count + 1
  iters[n] = count
  if n%2==0:
   n = int(n/2)
   print(n)
  else:
   n = int(3*n + 1) 
   print(n)
 print(count)
print(iters)
#Part B

  