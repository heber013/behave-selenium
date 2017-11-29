Selenium Tests using Behave
###########################
This is an example of selenium test using behave framework


Pre-requisites
==============
Ensure you have the following installed in the system:
Python3
pip3
virtualenv

Download chromedriver binary and make sure its location is in $PATH variable
(see https://sites.google.com/a/chromium.org/chromedriver/downloads)

To run the tests checkout the branch and follow the below steps
===============================================================
$ git clone https://github.com/heber013/behave-selenium
$ cd behave-selenium

On Linux systems:
$ ./run_tests
It will run all tests by default. You can specify behave filters, for example:
$ ./run_tests -t Example1
It will run the scenarios with tag @Example1

On Windows systems:
Make sure python3 is installed in the default location "C:\Python3\"
$ ./run_tests.bat
It will run all tests by default. You can specify behave filters, for example:
$ ./run_tests.bat -t Example1
It will run the scenarios with tag @Example1

*******************************************************************************
In this example has been used Page Object pattern.
This reduces the amount of duplicated code and means that if the UI changes,
the fix need only be applied in one place.
