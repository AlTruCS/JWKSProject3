# JWKS Project 2
Continuing on the previous Java Web Key Server, this uses SQLite in order to produce a clientside database file for the storage of private keys.

## Description
This continuation of the Java Web Key Server was programmed with the goal of adding the bare minimum to the complexity of the Project 1 base, with the only module addition to the main script being the required prerequisite of SQLite.

## Getting Started
To begin, run a terminal window and enter the following to ensure that SQLite is properly running the private key database:

```sqlite3 totally_not_my_privateKeys.db```

Once the process has started, load the ```main.py``` script using your IDE or terminal of choosing.

### Dependencies
* Python 3.11.8
* Cryptography 41.0.4
* Pyjwt 2.8.0
* SQLite 3.45.2
