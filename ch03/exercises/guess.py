import random

num = random.randrange(1, 11)
num_guesses = 0

for i in range(3):
  guess_num = int(input("Please enter a guess:"))
  num_guesses += 1
  if guess_num > num:
     print("Too High")
  elif guess_num < num:
      print("Too Low")
  else:
    print("Correct!")
    break
#print("It took you", num_guesses, "guesses to get it right.")

