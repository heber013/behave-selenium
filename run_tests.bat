PUSHD %~dp0
@ECHO OFF

cmd /c virtualenv --python=C:\Python3\python.exe ve
cmd /c ve\\Scripts\\activate
cmd /c ve\\Scripts\\pip3 install -r requirements.txt
cmd /c ve\\Scripts\\behave %*

cmd /c ve\\Scripts\\deactivate
