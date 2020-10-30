# Catcoder Attempts

Code storage for my past Catalyst Coding Contests attempts

## Requirements

* Install [Python](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper-win` (for windows)
* Run `set WORKON_HOME=%USERPROFILES%\Envs` (for windows)

## Set-up

* Run `git clone` this repository and `cd` into the project root.
* Run `mkvirtualenv venv` (for windows) or `virtualenv ../venv` (for mac or linux)
* Run `workon venv` (for windows) or `source ../venv/bin/activate` (for mac or linux)
* Run `pip install -r requirements.txt` to be able to use libraries like networkx.

## Run the programs

* To test the social network implementations, `cd` into the `social network` folder
* Run `python social_network_with_graph.py level1/level1_1.in level1/level1_1.out`
* Compare by running the same command with `social_network_with_networkx_graph.py` and `social_network3.py`
* Follow a similar command patterrn to run the rest.
