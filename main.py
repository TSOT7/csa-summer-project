# MAKE SURE THAT YOU RUN THE PROGRAM FROM THE SHELL USING THE CMD:
# 'python main.py'
import os


# Starts programs lists options
def startProgram():
  print("""
  ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝
                                                                 
  """)


  print("Welcome to my Program! \nWhat would you like to see")
  print("(1) About me\n(2) Interests\n(3) exit")

  nav = input("What would you like to do? Enter a number based on the menu above ↑\n")

  if "1" in nav:
    bio()
  elif "2" in nav:
    interests()
  elif "3" in nav:
    os.system('clear')
    exit()
  else:
    print('Error: Try again!')


# Choice functions 
def bio():
  
  os.system('clear')

  print("""
     █████████   █████                          █████   
  ███░░░░░███ ░░███                          ░░███    
 ░███    ░███  ░███████   ██████  █████ ████ ███████  
 ░███████████  ░███░░███ ███░░███░░███ ░███ ░░░███░   
 ░███░░░░░███  ░███ ░███░███ ░███ ░███ ░███   ░███    
 ░███    ░███  ░███ ░███░███ ░███ ░███ ░███   ░███ ███
 █████   █████ ████████ ░░██████  ░░████████  ░░█████ 
░░░░░   ░░░░░ ░░░░░░░░   ░░░░░░    ░░░░░░░░    ░░░░░  
                                                      
                                                      
                                                      
  """)
  
  print("""

  My name is Thomas. I am going to be a junior this year. 
  I have been in Milton my entire life. 
  I don't have a lot of special things planned for this summer but I am 
  currently branching out and doing a lot of things that 
  I normally wouldn't have time for. 
  I am always trying to learn something new and I am looking forward to this year! 
  
  
  """)
  returnText()

def interests():
  os.system('clear')
  print(""" 
  
    ███              █████                                         █████           
 ░░░              ░░███                                         ░░███            
 ████  ████████   ███████    ██████  ████████   ██████   █████  ███████    █████ 
░░███ ░░███░░███ ░░░███░    ███░░███░░███░░███ ███░░███ ███░░  ░░░███░    ███░░  
 ░███  ░███ ░███   ░███    ░███████  ░███ ░░░ ░███████ ░░█████   ░███    ░░█████ 
 ░███  ░███ ░███   ░███ ███░███░░░   ░███     ░███░░░   ░░░░███  ░███ ███ ░░░░███
 █████ ████ █████  ░░█████ ░░██████  █████    ░░██████  ██████   ░░█████  ██████ 
░░░░░ ░░░░ ░░░░░    ░░░░░   ░░░░░░  ░░░░░      ░░░░░░  ░░░░░░     ░░░░░  ░░░░░░  
                                                                                 
                                                                                 
                                                                                 
  """)

  print("""My main interests are technology and cars.
  
  Here are some cool things about me: 

  • I am currently in the process of learning linux. I plan on using it for productivity purposes

  • I am learning a new keyboard layout (colemak) 

  • I am in the process of creating a blog/portfolio site

  • I am getting a lot of driving hours done for my license 

  • I can speak english, cantonese, and a little bit of mandarin


  """)

  returnText()

def returnText():
  what = input("""
  would you like to return to the main menu?
  Would you like to go to another section of this project?
  Would you like to exit this program?
  
  1(Go back to main menu) 2(Exit the program)

  """)



  if "1" in what:
    os.system('clear')
    startProgram()
  elif "2" in what:
    quit()
  

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


