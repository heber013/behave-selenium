Selenium Tests using Behave
###########################
This is an example of selenium test using behave framework.
You can execute tests using docker-compose with a single command, or run tests locally.
The following sections describe both options.

Running tests using docker-compose
==================================
1- Install docker-compose in your system, then:

::

  $ git clone https://github.com/heber013/behave-selenium
  $ behave-selenium
  $ sudo docker-compose up --build

It will create the selenium grid run all the tests in a docker container.
First execution is slow since docker-compose has to download all the images.

|

Then you can run another command inside a specific container from the docker-compose.yaml,
for example to run all tests against firefox:

::

    $ sudo docker-compose run ui_tests -b firefox -g http://selenium_hub:4444/wd/hub

Run command, in this case, will not build the images. To build a specific image run:

::

    $ docker-compose build ui_tests

After the execution, it’s possible to stop the running containers and delete them with a command:

::

    $ docker-compose down


Running tests in the local machine
===============================================================
1- Install Python3, pip3, virtualenv

::

    $ git clone https://github.com/heber013/behave-selenium
    $ cd behave-selenium

If you want to run the tests using standalone drivers,
make sure you have the corresponding driver in a location present in $PATH:

::

    $ ./run_tests

By default, it runs against chrome browser, but you can change it using '-b' or '--browser' option:

::

    $ ./run_tests -b firefox

If you have a selenium grid, you can specify it with '-g' or '--grid' option:

::

    $ ./run_tests -g http://^GRID_URL^:4444/wd/hub
