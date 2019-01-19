# Password Manager

### Installation

Has been tested on Fedora 28, Python version 3.6.5

Install the dependencies

```sh
$ pip3 install cryptography
```

(For fedora users xsel- clipboard tool is required)
```sh
$ sudo dnf install xsel
```

### Usage

Open your favorite Terminal and run these commands.

To create a password for a new account:
```sh
$ python3 password.py create [account_name]
```

To encrypt and store an existing password:
```sh
$ python3 password.py encrypt [account_name]
$ Type existing password to encrypt and store: [Your_password]
```

To retrive a stored password:
```sh
$ python3 password.py get [account_name]
$ password for [account_name] is copied to your clipboard.
```

To retrive the list of accounts with stored passwords:
```sh
$ python3 password.py show all
```
To delete a stored password:
```sh
$ python3 password.py delete [account_name]
```
All the passwords are encrypted and stored alongside the account name, in the 'encrypted_data.bin' file, which is created in the same directory.
