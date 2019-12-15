import tkinter as tk
import  os
import webbrowser



root = tk.Tk()
root.title("Automate 3 functions")

def github():
    webbrowser.open_new_tab("github.com")

button1 = tk.Button(root,text="open github",width= 25,command = github)
button1.pack()

def code():
    os.system("code")

button2 = tk.Button(root,text="Start vs code", width = 25, command= code)
button2.pack()

def checkmail():
    webbrowser.open_new_tab("gmail.com/inbox")

button3 = tk.Button(root,text="Check your email",width= 25,command =checkmail )
button3.pack()



root.mainloop()
