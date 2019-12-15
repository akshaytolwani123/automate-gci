import os

file = open(".bashrc","a")
file.write("echo Running at boot\n")
file.write("python3 automate-gci/automate-gci.py")
file.close

os.system("rm -rf automate-gci/startupadd.py")