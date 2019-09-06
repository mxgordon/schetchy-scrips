import pxssh 
import getpass 

#login to ssh
def ssh():
  try:
    s = pxssh.pxssh()
    hostname = input('hostname:')
    username = input('username:')
    password = getpass.getpass('pasword:')
  except Exception as e:
    print(e)
  if s.login(hostname, username, password):
    if not s.login(hostname,username,password):
      print('sorry try again. Those creds were incorrect...')
    #I think
    #actually sending shit to the connected device
    s.sendline(input('>'))
    s.prompt
    print(s.before)
    #logging out
    if input() == "I don't wanna play with you anymore":
      s.logout()
    
    #hoping that the goto line will work as a repeat command 