# verificationTweets
## Requirements:

 - python version >=3.5
 - pip3
Install and upgrade using:	
```sh
$ pip3 install --upgrade pip
```

## Steps
Firstly I recommend installing virtualenv and creating a virtual environment
```sh
$ sudo apt-get install python3-venv
```
Then create a source directory to store the environment
```sh
$ mkdir project
$ python3 -m venv /path/to/project
```
Now to activate, use the following line
```sh
$ source /project/bin/activate
```
After the virtual env is set up and activated you will need to install all dependencies for the project
```sh
(project) $ pip3 install -r requirements.txt
```
This will ensure all packages are correctly installed, NLTK will require some extra downloads to fix this
```sh
(project) $ python3 
(project) $ >> import nltk
(project) $ >> nltk.download('all')
```
This is the easiest way to get set up and running, but time consuming as it will download all corpa from NLTK

## To run
To run the project make sure that the venv is activated and type:
```sh
(project) $ export FLASK_APP=webpage.py
(project) $ flask run
```

This tells flask what to run, webpage.py will only run if the template and static directories are present
The command line output will direct you to the local webpage to put into any browser


## Change modes
You will need to edit devTweet.py through the main() function, uncomment what type of classifier you would like
After it has retrained relaunch the webpage with flask and the results should be from the most recently trained model
