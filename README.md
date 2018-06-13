Password-Manager

Console based program to create new passwords. These passwords after encryption are stored in a file, along with the account name.
Data stored in 'encryption_data.bin' in the same directory.

Installation :

import the password.py file.
 
$ pip3 install cryptography

for fedora distribution:
$ sudo dnf install xsel

Usage: 

To add a new account:
$ python3 password.py create [account_name]

To retrive a stored password:

$ python3 password.py get [account_name]



