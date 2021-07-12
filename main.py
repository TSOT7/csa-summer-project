



# Starts programs lists options
def startProgram():
  print("Welcome to my Program! \nWhat would you like to see")
  print("(1) About me\n(2) Interests\n(3) exit")


# Choice functions 
def bio():
  
  print("About Me")
  
def interests():
  
  print("Interests")

def exit():
  
  print("Farewell")




startProgram()

nav = input("What would you like to do? Enter a number based on the menu above ↑\n")

if "1" in nav:
    bio()
elif "2" in nav:
    interests()
elif "3" in nav:
    exit()
else:
  print('Error: Try again!')


