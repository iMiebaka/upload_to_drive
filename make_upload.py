
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
   
# For using listdir()
import os
   
  
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
   
# replace the value of this variable
# with the absolute path of the directory
path = r"C:\Games\Battlefield"   
   
# for x in os.listdir(path):
   
   