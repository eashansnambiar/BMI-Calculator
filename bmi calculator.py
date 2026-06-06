weight=float(input("Enter your  weight in KG"))
height=float(input("Enter your  height in Metres"))
bmi=weight/(height*height)
print("your BMI is: " +str(bmi))
if bmi>25:
  print("You are obesse")
elif bmi<18.5:
  print("you are under weight")
elif 18.5<= bmi <=25:
  print("you are normal")

  

