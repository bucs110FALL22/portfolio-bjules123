print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15) #the answer is a infinite repeating decimal but in the shell it stops


rate = float( input("What is the current rate for the Euro to Dollar?"))
print(rate, type(rate))

amount = float( input("What is the amount of currency to exchange?"))
print(amount, type(amount))

total = (rate*amount)
result = total-3
print(result)