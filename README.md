# verificationTweets
Requirements:
	python version >=3.5
	pip3
	Install and upgrade using:	
	$ pip3 install --upgrade pip

Steps:
	Firstly I recommend installing virtualenv and creating a virtual environment:
	$ sudo apt-get install python3-venv

	Then create a source directory to activate the environment:
	$ mkdir project
	$ python3 -m venv /path/to/project

	Now to activate, use the following:
	$ source /project/bin/activate

	After the virtual env is set up and activated all dependencies for the project
	$ pip3 install -r requirements.txt
	
	This will ensure all all packages are corrected installed, NLTK will require some extra downloads to fix this:
	$ python3 
	$ >> import nltk
	$ >> nltk.download('all')
	
	This is the easiest way but time consuming as it downloads all corpa from NLTK

To run:
	To run the project make sure that the venv is activated and type:
	$ export FLASK_APP=webpage.py
	$ flask run

	This tells flask what to run, webpage.py will only run if the template and static directories are present
	The command line output will direct you to the local webpage to put into any browser


To change modes:
	You will need to go into devTweet.py and under main() uncomment what type of classifier you would like
	After it has retrained relaunch the webpag with flask and the results should be from the most recently trained model
