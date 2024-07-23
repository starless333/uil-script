# uil-script
Simple file to provide structure to your UIL Contests!
# What it does
It simply takes all the data files (dat) and creates directories based on the names. It designates a directory for each data file copies a Makefile from ~ and copies it into the new directory in case you want to run the java file with make. 
# How to run
```bash
python3 script.py
```
# Optional
You can put the following into your ~/.bashrc or ~/.zshrc or whatever you run. 
```bash
alias uil="python3 ~/uil-script/script.py"
```
This allows you to just type uil and have it execute over your current dir. 
