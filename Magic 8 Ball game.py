import random


print("Hello!, Do you want to know if you will be rich?")
print("Please insert a number btween 1 - 9.")

ask = input("input number: ")
name = "You"
question = "Will I become rich?"
answer = ""

random_number = random.randint(1, 9)
if random_number == 1:
  answer ="Yes - definitely"
elif random_number == 2:
  answer = "Not so sure"
elif random_number == 3:
  answer = "Not in a milion years"
elif random_number == 4:
  answer = "In 50 years if you work in 2 jobs!"
elif random_number == 5:
  answer = "Yes in year 3000 hhhh"
elif random_number == 6:
  answer = "Yes, if you learn how to code"
elif random_number ==7:
    answer = "Dont even think about it"
elif random_number == 8:
   answer = "YES of course if you invest your moeny in crypto"
elif random_number == 9:
  answer = "Keep trying, one day you may"
else:
  answer = "Error"
  
print (name + " asked: " + question)
print ("Magic 8-Ball's answer: " + answer)
  
if name == "":
  print("Question: " + question)
if question == "":
    
  print("Provide question, otherwise, the fabric of reality is at risk!")
