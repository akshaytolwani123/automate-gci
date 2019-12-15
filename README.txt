# automate-gci
Note:- This only works on linux
This is a gui program to automate any 3 tasks at startup
First clone the repository in your home directory.Do not clone it in any other directory as it will not work
cd into automate-gci/
run python3 startupadd.py to add the gui to startup
It will write two lines to your .bashrc to launch the gui at startup
It will be added to startup
run python3 automate-gci.py to launch it
To remove it from startup delete the last last two lines from your .bashrc file

The gui automates 3 tasks. They are:-
1.Launch github
2.Launch vs code
3.Launch gmail webiste

The modules used are:-
webbrowser
os
tkinter
