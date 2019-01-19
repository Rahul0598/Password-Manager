#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:41:32 2018

@author: devajji
"""

import string,random,os,time,sys,pyperclip,linecache
from cryptography.fernet import Fernet

def getpw():
  found = False
  with open(file_name,'r+b') as f:
    for line in f:
      if line.startswith(account):        
        found = True
        encrypted_pw = line.split(link)[1]
        decrypted_pw = cipher.decrypt(encrypted_pw)
        pyperclip.copy(decrypted_pw.decode())
        print('Password for '+account.decode()+' is copied to clipboard.')
        time.sleep(6)
        os.system("xsel -b --delete")
        return
  if not found:
  	print('not found')
  	return

def createpw():
  with open(file_name,'r+b') as f:
    for line in f:
      if line.startswith(account):
        print('already exists')
        getpw()
        return
  set = string.ascii_letters + string.digits + string.punctuation
  while True:
    password = ''.join(random.choice(set) for i in range(30))
    if (any(c.islower() for c in password)
      and any(c.isupper() for c in password)
      and sum(c.isdigit() for c in password) >= 3):
  	  break
  password = password.encode('utf-8')
  encrypted_password = cipher.encrypt(password)
  entry = account + link + encrypted_password
  with open(file_name,'a+b') as f:
    f.write(entry)
    f.write(b'\n')
  print('Password created')
  return

def showStored():
  l = 0
  with open(file_name,'r+b') as f:
  	for line in f:
	    if l == 0:
	      l = l + 1
	      continue
	    account = line.split(link)[0]
	    account = account.decode()
	    print(account)
  return

def encrypt():
  with open(file_name,'r+b') as f:
    for line in f:
      if line.startswith(account):
        print('already exists')
        getpw()
        return
  password = input("Type existing password to encrypt and store: ")
  password = password.encode('utf-8')
  encrypted_password = cipher.encrypt(password)
  entry = account + link + encrypted_password
  with open(file_name,'a+b') as f:
    f.write(entry)
    f.write(b'\n')
  print('Password created')
  return

def delete():  
  found = False
  f = open(file_name,'r+b')
  lines = f.readlines()
  f = open(file_name,'w+b')
  for line in lines:
    if line!=line.startswith(account):        
      found = True
      f.write(line)
      f.close()
      return
  if not found:
    print('not found')
    return

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python3 password.py [create/get/encrypt] [account]')
  file_name = 'encrypted_data.bin'
  line = linecache.getline(file_name, 1)
  if not line:
    with open(file_name,'a+b') as f:
      cipher_key = Fernet.generate_key()
      f.write(cipher_key)
      f.write(b'\n')
  choice = sys.argv[1]
  account = sys.argv[2]
  account = account.encode('utf-8')
  key = line[:-1].encode('utf-8')
  cipher = Fernet(key)
  link = b':'
  if choice == 'create':
    createpw()
  elif choice == 'get':
    getpw()
  elif choice == 'show':
    showStored()
  elif choice == 'encrypt':
  	encrypt()
  elif choice == 'delete':
    delete()
  else:
    print('invalid option')
