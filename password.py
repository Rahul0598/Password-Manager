#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:41:32 2018

@author: devajji
"""

import string
import random
import os.path
import time
import sys
import pyperclip
import linecache
from cryptography.fernet import Fernet


def getcipher():
    line = linecache.getline(file_name, 1)
    key = line[:-1].encode('utf-8')
    return Fernet(key)


def account_exists():
    with open(file_name, 'r+b') as f:
        for line in f:
            if (account + link) in line:
                print('already exists')
                decrypt(line)
                return True


def decrypt(line):
    encrypted_pw = line.split(link)[1]
    decrypted_pw = getcipher().decrypt(encrypted_pw)
    pyperclip.copy(decrypted_pw.decode())
    print('Password for ' + account.decode() +
          ' is copied to clipboard.')
    time.sleep(6)
    os.system("xsel -b --delete")


def getpw():
    found = False
    with open(file_name, 'r+b') as f:
        lines = f.readlines()
        for line in lines:
            if (account + link) in line:
                found = True
                decrypt(line)
    if not found:
        print('not found')
        return


def createpw():
    if not account_exists():
        set = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(set) for i in range(30))
            if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                    sum(c.isdigit() for c in password) >= 3):
                break
        password = password.encode('utf-8')
        encrypted_password = getcipher().encrypt(password)
        entry = account + link + encrypted_password
        with open(file_name, 'a+b') as f:
            f.write(entry)
            f.write(b'\n')
        print("Password Created")


def showStored():
    c_lno = 0
    with open(file_name, 'r+b') as f:
        for line in f:
            if c_lno == 0:
                c_lno = c_lno + 1
                continue
            account = line.split(link)[0]
            account = account.decode()
            print(account)


def encrypt():
    check_account()
    password = input("Type existing password to encrypt and store: ")
    password = password.encode('utf-8')
    encrypted_password = getcipher().encrypt(password)
    entry = account + link + encrypted_password
    with open(file_name, 'a+b') as f:
        f.write(entry)
        f.write(b'\n')
    print('Password created')


def delete():
    password = account + link
    with open(file_name, 'r+b') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if password not in line:
                f.write(line)
        f.truncate()
    print("Password deleted.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 password.py [create/get/encrypt] [account]')
    file_name = 'encrypted_data.bin'
    if not os.path.isfile(file_name):
        f = open(file_name, 'w+b')
        cipher_key = Fernet.generate_key()
        print("file created")
        f.write(cipher_key)
        f.write(b'\n')
        f.close()
    choice = sys.argv[1]
    account = sys.argv[2]
    account = account.encode('utf-8')
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
