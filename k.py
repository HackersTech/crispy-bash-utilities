#powered by hackers tech 
# samajik sandesh --be happy

import os

print(" link of our youtube channel in repo")
print ("\033[3;37m file should be in working directory/ or give folder path")
print("if you are in Linux put the text file in single quote ex- 'k.txt' ")
l=input("Enter file name to seperate password from file ")
if l!="":
    k=open(l,'r')
    try:
                h=' '
                while h:
                        h=k.readline()
                        g=h.split(":") #seprator may be different as your needs you can change it
                        print(g[1])
    except:
                k.close()

else:
    print('\033[5;31m error occured invalid input')
    print("\033[5;35m starting again")
    os.system("python k.py")
