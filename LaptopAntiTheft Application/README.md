# CyberHawk : Anti-Theft Application for Windows Laptops
[![Build Status](https://travis-ci.org/Ash-Shaun/CyberHawk.svg?branch=master)](https://travis-ci.org/Ash-Shaun/CyberHawk)
[![Requirements Status](https://requires.io/github/Ash-Shaun/CyberHawk/requirements.svg?branch=master)](https://requires.io/github/Ash-Shaun/CyberHawk/requirements/?branch=master)
[![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Ash-Shaun/CyberHawk/blob/master/LICENSE)
[![Compatibility](https://img.shields.io/badge/python-3-brightgreen.svg)](https://github.com/Ash-Shaun/CyberHawk)

Laptops change the ways of communication, it provides an advantage of communicating with anyone virtually through video conferencing, email, etc., and it also provides a facility to store contact numbers, email id’s, in memory which reduces the concept of File-System to store personal information. Company related information and documents can be viewed anywhere and can be shared with anyone. Because of its <b>light weight</b> and <b>small size</b>, it can be stolen very easily and the confidential-information of any organization or personal details of people stored in the phone memory can be easily exposed. My project's aim is to put forward a technique through which the thief, who steals any laptop installed with <i>CyberHawk</i>, gets captured and the user can make him/her stop misusing any confidential information. This application includes Socket communication, Reverse TCP where you can send video clips and photos to  owner even under a firewall, unlike Email which includes only text. It gives the information about the thief by sending the snapshots and a small video clip of the thief to an alternate account, which helps us to recognize the thief.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Python 3.5
2. PyQt 5.6
3. MySQL ([XAMPP](https://www.apachefriends.org/download.html) Server Preferred)

The complete Prerequisite can be obtained from [requirements.txt](https://github.com/Ash-Shaun/CyberHawk/blob/master/requirements.txt)

### Installing

CyberHawk can run on Python 3.5. 

Before you proceed to start the application, you need to change the DB variables to suite your needs
```
#Change line <b>89</b> in /CLIENT/main.py
#Change line <b>5</b> in /MASTER/db.py
db = MySQLdb.connect("localhost","<username>","<password>","<DB name>")
```

OPTIONAL: phpMyAdmin SQL Dump of DB I used during development
```
#You can import it through phpMyAdmin if you need
Filename: credentials.sql
DB name: credentials
Table name: Master , Client
```

```
# To open Client window
$ cd CLIENT/
$ python main.py
```
## Screenshots

Client

![Client](https://raw.githubusercontent.com/Ash-Shaun/CyberHawk/master/client.JPG)

Master

![Master](https://raw.githubusercontent.com/Ash-Shaun/CyberHawk/master/Master.JPG)
![Master](https://raw.githubusercontent.com/Ash-Shaun/CyberHawk/master/master2.JPG)


## Usage

```
# To open Client window
$ cd CLIENT/
$ python main.py

# To open Master window
$ cd MASTER/
$ python main.py
```

## Deployment

This project is still in dev-bench. I will be working in my spare time to make it fully production ready. I am open to any kind of collaboration make this project reach production level 

## Built With

* [PyQT](https://riverbankcomputing.com/software/pyqt/intro) - GUI framework
* [Requests](https://docs.python-requests.org/) - Do I need to tell you more about it ;)

## Contributing

All contributions are welcome. :)

## Authors

* **Aslam Muhammed** - <i> Ideator, worker, debugger,... </i> [Ash-Shaun](https://github.com/Ash-Shaun)

## Troubleshooting

1. MySQLdb may have a compatibility issue with Python 3.x . Also some users reported they were not able to install MySQLdb through pip.
```
#Solution:
$ pip install pymysql

#change the import statement

#import MySQLdb -> import pymysql
```

## Contributors

<i> None so far...</i>

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Log0 - <im.ckieric@gmail.com>
* Arjun Gullbadhar - <https://github.com/arjunfzk>

