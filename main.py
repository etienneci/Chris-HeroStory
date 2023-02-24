# Intro
print("**// Hero Origin: Rebirth \\**")
print()
print("Your eyes slowly open and light enters your view. As your vision focuses, you notice a strange ball of energy floating above you. You reach out and touch the light, and as you do a voice in your head suddenly proclaims:") 
print()
print("YOU HAVE BEEN CHOSEN FOR A SECOND CHANCE. A SECOND LIFE. WHAT LIFE WILL YOU LEAD? WHAT KIND OF HERO WILL YOU BE?!")
print()
print()

# Pick a story
# question 1
# get user path selection

print("** What life will you choose? **")
print()
print("a. An alien physiology, granting the ability of super strength, flight, durability, and heat/enhanced vision.")
print()
print("b. A connection to a force of power, granting the ability to move faster than light and phase your molecules through solid objects.")
print()
print("c. A body that is half machine, granting the ability to interface with anything that is electronic, and even augment your own body with other technology. ")
print()

# option 1 - superman story
# display story for option one
option = input("Please select a life and power: ")
print()

if option == "a":
  print("You decide on a path and live on as Superman. It has been a few years and you are thriving as the world's most powerful hero. There is a mission from The Watchtower for you to investigate a trap left by Lex Luthor. You must find it, but be careful, this may all be a trap for you...")
  print("You've narrowed it down to 3 locations: ")
  print("a. Metropolis")
  print()
  print("b. Gotham")
  print()
  print("c. Star City")
  print()
  location = input("Please select where to search: ")
  print()

  # get user choice and check if correct
  if location == "a":
    print("Watchtower: OH NO!! IT WAS A TRAP! KRYPTONITE!!!")  
    
  elif location == "b":
    print("After searching through the streets of Gotham, and with the help of Batman and the Bat Family, you manage to find and deactivate the explosive. But there's no sign of Luthor...only...Gorilla Grodd!?!? What is going on?")
  else:
    print("Watchtower: OH NO!! IT WAS A TRAP FOR YOU! KRYPTONITE!?")

# option 2 - flash story
# display story for option 2  
elif option == "b":
  print("So you decided on the path of the speedster and lived on known as The Flash. You spent years saving many people and stopping countless crimes as you can move so fast and efficiently. Unfortunately, your rogues gallery knows that all to well. Captain Cold has contracted the help of the Riddler and they managed to capture you.")
  
  print()
  print("There is only one way out of this, Flash. I think you know...")
  print()
  print("I am flora, not fauna. I am foliage, not trees. I am shrubbery, not grass. What am I?")
  print()
  riddleAnswer = "bush"
  userAnswer = input("I am... : ")
  print()

  # get user answer and check if correct  
  if userAnswer == riddleAnswer:
    print("Riddler: Impressive!! Sorry Captain Cold. You're on your own.")
    print("Captain Cold: That's cold...")
    print()
  elif userAnswer == "Bush":
    print("Riddler: Impressive!! Sorry Captain Cold. You're on your own.")
    print("Captain Cold: That's cold...")
    print() 
  else:
    print("Riddler: WRONG! Hah! That was a tough one wasn't it. You've got nothing on the Bat!")
    print("Captain Cold: I may not be able to beat you, Flash, but even I knew that one!!")
    print()

# option 3 - cyborg story
# display story for option 2
elif option == "c":
  print("You have chosen the path of advanced tech and live as a hero named Cyborg. Your abilities are unmatched in a society that runs on information. An very loud evil genius has manged to infect you with a virus, has hidden a secret code in an incredibly simple problem. You must crack the code to free your systems!")
  print()
  print("$ Dr. Code: HAHA I have hijacked your central processing unit, Cyborg? You will never be free unless you crack the code!")
  print()
  
  # get user amswer
  numAnswer = 14
  print("x = 6 + 10 - 2")
  userAnswer = input("Virus: Please enter your answer. Time is running out. What is x: ")
  userAnswer = int(userAnswer)
  print()

  # check if correct and display outcome
  if userAnswer == numAnswer:
    print("Dr. Code: PSHHHAAH!! I guess you're smarter than I thought! You win this time! I am getting out of here before your systems come back online!")
  else:
    print("Dr. Code: HAHA! You fool, that is incorrect!! Now the virus will spread to every machine in on the net!!")
    
