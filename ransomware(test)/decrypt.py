#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet	#library for encryption


#FILTER FOR THE REATTACK - let's find some files

files=[]

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file =="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)	
print(files)

#READING THE SECRET KEY
with open("thekey.key","rb") as key:
	secretkey = key.read()

#USER PHRASE CHECK
secretphrase="coffee"
user_phrase=input("Enter the secret phrase to decrypt your files:\n")


#OPEN the KEY-file and SAVE ITS CONTENT into the variable
if user_phrase == secretphrase:
	for file in files:
		#Extract content of the each file
		with open(file,"rb") as rfile:
			contents= rfile.read()
		#Decrypt content of the each file
		contents_decrypted= Fernet(secretkey).decrypt(contents)
		#Write decrypted_content to original file
		with open(file,"wb") as rfile:
			rfile.write(contents_decrypted)
