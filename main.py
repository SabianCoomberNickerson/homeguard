# Copyright (C) 2014 Vitanoxi <Vitanoxi@gmail.com>

#Login
 
import time
import logging
  For name
print('Please enter your username.')
 
name=input()
 
#the three types of users, chnage the names and the password. They act as two codes, the username is a perm based password 
#giving the user a perm, the second is the system wide code, for any changes made
username=  {
'Admin',
'User',
'Moderator'
} 
if name == (username):
        print('Please wait')
        time.sleep(1.5)
        print('')
        print('Correct, please enter your password.')
 
password=input()
 
enterpassword='pass'
if password == (enterpassword):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome '+username)
        time.sleep(10)
#Logs people that have logged into the console
        logging.basicConfig(filename='previouslogins.log',level=logging.DEBUG)
        logging.debug(time + username + " has logged in")
        
 
if name != (username):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Incorrect, closing program.')
        time.sleep(1.5)
        exit

#Command Structure:
#Admin
#Mod
#User
if name == (Admin)
        set group 'Admin'
        
if name == (Moderator)
        set group 'Mod'        

if name == (User)
        set group 'User'        

#executes commands for the script files

command=input()

commands={
'admin',
'laser',
'upload',
'light',
'start',
'stop'
}
#Put this in to make it simple
if command==(admin):
          print('Please wait')
          time.sleep(1.5)
          print(Please Enter Admin Password!)
          adminpassword=input()
          if adminpassword == (Admin):
                           set group 'Admin'
          
if command==(laser):
          print('Please wait')
          time.sleep(1.5)
          execfile("laser.py")
          print('Executing command')
          logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
          logging.debug(time + username + "has used the laser command")

if command==(light):
          print('Please wait')
          time.sleep(1.5)
          execfile("light.py")
          print('Executing command')
          logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
          logging.debug(time + username + "has used the light command")
          
if command==(upload):
          print('Please wait')
          time.sleep(1.5)
          execfile("upload.py")
          print('Executing command')
          logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
          logging.debug(time + username + "has used the upload command")

if command==(start):
          print('Please wait')
          time.sleep(1.5)
          execfile("start.py")
          print('Executing command')
          logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
          logging.debug(time + username + "has used the start command")          

if command==(stop):
          print('Please wait')
          time.sleep(1.5)
          execfile("stop.py")
          print('Executing command')
          logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
          logging.debug(time + username + "has used the stop command")
          
if command!=(commands):
          print 'Please Wait'
          sleep (1.5)
          print 'No Such Command Please Try Again'
