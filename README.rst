Selenium Tests using Behave
###########################
This is an example of selenium test using behave framework


Pre-requisites
==============
Install in the system:
- Python3
- pip3
- virtualenv
- chromedriver binary in a location that is in $PATH

To run the tests checkout the branch and follow the below steps
===============================================================
$ git clone https://github.com/heber013/behave-selenium
$ cd behave-selenium

On linux systems:
$ ./run_tests
It will run all tests by default. You can specify behave filters, for example:
$ ./run_tests -t Example1
It will run the scenarios with tag @Example1

On Windows systems:
$ ./run_tests.bat
It will run all tests by default. You can specify behave filters, for example:
$ ./run_tests.bat -t Example1
It will run the scenarios with tag @Example1
