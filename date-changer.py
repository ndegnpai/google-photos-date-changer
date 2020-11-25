import os
import time
import datetime
import subprocess


months = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with os.scandir('.') as folders:
    for folder in folders:
        if os.path.isdir(folder):
          #print(folder.name)
          date = folder.name[:10]
          date = date.split("-")
          print("ENTERING FOLDER: " + folder.name)
          with os.scandir(folder.name) as files:
              print ("Files in " + folder.name)
              for file in files:
                  print(file.name)
                  path = folder.name + "\\" + file.name
                  new_date = date[2] + " " + months[int(date[1]) - 1] + " " + date[0] + " 5:00 PM"
                  os.system ("powershell.exe -command \"(Get-Item -literalpath '" + path + "').creationtime=('" + new_date + "'); (Get-Item -literalpath '" + path + "').lastaccesstime=('" + new_date + "'); (Get-Item -literalpath '" + path + "').lastwritetime=('" + new_date + "')\"")
