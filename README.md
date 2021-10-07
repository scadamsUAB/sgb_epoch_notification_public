# sgb_epoch_notification

This code was put together using an Ubuntu 18.04 operating system.  It is possible some changes from what is described below may be needed if you do not use the same OS. 

The webscraping portion of the project uses selenium with firefox so you will need firefox installed as well as the geckodriver

To install the geckodriver use sudo apt-get install firefox-geckodriver

The requirements.txt file can be used to install all required packages.  It is suggested to use a virutal environment for the installation of the packages and running of the code.  

All packages should be stored in requirements.txt


There are two main parts of the application.  

epoch_announcer.py will open a Selenium instance to navigate to the Songbird block explorer and check for the eooch to change.  If it changes it will increment the epoch check and send a message using twitter and discord based on values in the config file. If the the epoch is not changed it will wait and then save an entry to the log.txt file with the last time the check occured and the current epoch value. 

app.py is a flask web app to act as a front end check to verify the application is still running.  It will check the log.txt file and print out the value to the web browser. 

