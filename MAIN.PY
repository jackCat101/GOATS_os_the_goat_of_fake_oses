import os
print("""
   _____  ____       _______ _____ 
  / ____|/ __ \   /\|__   __/ ____|
 | |  __| |  | | /  \  | | | (___  
 | | |_ | |  | |/ /\ \ | |  \___ \ 
 | |__| | |__| / ____ \| |  ____) |
  \_____|\____/_/    \_\_| |_____/ os
""")
if input("Login or add user: ") == "add user":
    file = open("users/" + input("Name: ") +".txt", "w")
    file.write(input("password: "))
    file.close()
else:
    file = open("users/" + input("username: ") + ".txt", "r")
    contents = file.read()
    iscorect = False
    while not iscorect:
        iscorect = input("pass: ") == contents
        if iscorect == False:
            print("Wrong pass!")
        
    