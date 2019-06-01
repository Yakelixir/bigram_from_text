#!/usr/bin/env bash

# Check for python3 or fail the startup

echo

read -p "This script will check if you have python installed,
create a virtualenv, and install dependancies. Do you want to continue? [Y/n]" userInput

# Check if string is empty using -z. For more 'help test'
if [[ $userInput == 'Y' ]]; then
    # If userInput is not empty
    if command -v python3 &>/dev/null; then
        echo CHECK: Python 3 is installed so lets set up a virtual env...
        if command -v virtualenv &>/dev/null; then
            echo CHECK: virtualenv is installed!
            echo BUILD: Lets set up a vitualenv [nltk_vrtenv]
            virtualenv nltk_vrtenv # create a virtualenv for pip to install into
            source $PWD/nltk_vrtenv/bin/activate # activate the virtualenv
            echo CHECK: nltk_vrtenv should be built and lets start installing
            echo BUILD: Running pip to install requirements
            pip install -r $PWD/config/requirements.txt
            chmod +x nltk_setup.py
            ./nltk_setup.py
        else
            echo Virtualenv is not setup. Please install this and attempt this once that is completed
            exit 1
        fi
    else
        echo Python 3 is not installed. Please install this and attempt this once that is completed
        exit 1
    fi
else
    echo Exiting... We can have some bigram fun later when your ready to setup. Never rush quality!
    exit 1
fi