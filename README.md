# TechNova '22: Join the Club!
Join the Club! is a web application that allows busy university students to keep track of club application deadlines. By simply inputting your Instagram account credentials and the Instagram username of the club you would like to join, this web app will provide you with crucial details about when to apply.

For more information, visit: https://devpost.com/software/join-the-club

## Table of Contents
* [Setup](#setup)
  * [For Linux](#for-linux)
  * [For MacOS](#for-macos)
  * [After Installing Initial Requirements](#after-installing-initial-requirements)
  * [Set Environment Variables](#set-environment-variables)
* [How to Use This Project](#how-to-use-this-project)

## Setup 
### For Linux
If Python has not been previously installed, run the following:
```
$ sudo apt install python3.9
$ python3.9 --version
```
If pip has not been previously installed, run the following:
```
$ sudo apt-get install python3-pip 
$ pip3 --version
```

### For MacOS
If Homebrew has not been previously installed, follow the instructions listed [here](https://brew.sh/).

If Python has not been previously installed, run the following:
```
$ brew install python@3.9
$ python3.9 --version
```
If pip has not been previously installed, run the following:
```
$ python3.9 -m ensurepip --upgrade
$ pip3 --version
```

### After Installing Initial Requirements
If Google Chrome has not been installed on your local machine, download the Chrome installer [here](https://www.google.com/intl/en_ca/chrome/).

Clone this repository:
```
$ git clone <technova URL>
``` 
When asked to enter credentials, input your username and personal access token.

Install the required dependencies included in requirements.txt:
```
$ pip3 install -r requirements.txt
```

### Set Environment Variables
Create a copy of .env.template named .env:
```
$ cd technova
$ cp .env.template .env
``` 
Open the newly created file and fill in the variables:
```
INSTAGRAM_USERNAME=""
INSTAGRAM_PASSWORD=""
INSTAGRAM_CLUB_USERNAME=""
``` 
**INSTAGRAM_USERNAME**\
Assign your Instagram username to this variable. 

**INSTAGRAM_PASSWORD**\
Assign your Instagram password to this variable. 

**INSTAGRAM_CLUB_USERNAME**\
Assign a club's Instagram username to this variable. 

## How to Use This Project
<img align="right" width="275" src="https://github.com/miaisakovic/technova/blob/main/images/icon.png">

Each time you would like to recieve information on a club's application deadlines, run the following command:
```
$ python3.9 <relative path to club_info.py>
```

Each time you would like to view the UI for this project, run the following command:
```
$ python3.9 <relative path to join_the_club.py>
```
