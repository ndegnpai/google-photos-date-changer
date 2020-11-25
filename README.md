# google-photos-date-changer
Change (created, modified, accessed) date from photos downloaded with google takeout.

Google photos takeout archive will contain folders with name as a date and also folders created by google photos assistant. 
The problem is that in some folders the timestamp of the photos is different than the date from folder name.
I needed to upload my photos to a NAS and those were wrongly indexed. The program will change the date from files with the date from the folder name.

Just run the python script in your Google Photos folder. 

ex: python date-changer.py

I have also created an exe file. 

The program will work only on Windows operating systems with powershell. 
