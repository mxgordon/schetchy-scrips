#this is the launcher for other programs. Gonna use it for scripts and other tools. 

# from ssh import ssh
import sys, os

print ('Welcome to my program. I hope you enjoy!')
print ('what do you want to do?')

# list 
print ('1: linux script') #60% chance this shit works 
print ('2: windows script') #WIP (doesn't exist)
print ('3: ssh bullshitery') #WIP 
print ('4: review the checklist') #WIP

# this is the variables that will launch the programs.
usrinput = input()
compoutput = int(usrinput)
if compoutput == (1):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  print(dir_path)
  os.system('./linux.sh')
  # os.system('linux.sh')
if compoutput == (2):
  print ("hold your horses hombre, this isn't quite ready. Come back in a little bit.")
if compoutput == (3):
  pass
  #ssh()
if compoutput == (4):
  with open("checklist.txt","r") as f: 
   print (f.read())