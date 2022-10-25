
letterA= "A"
letterB= "B"
letterC= "C"
letterD= "D"
letterF= "F"

def percentage_to_letter(score=0):
  score = float(input("What grade?"))
  if score > 90:
   return letterA
  if score in range(80, 90):
    return letterB
  if score in range(70, 80):
   return letterA
  if score in range(60, 70):
    return letterB
  if score <60:
    return letterB
print(score)