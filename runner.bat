set SQUISHPATH="C:\Users\training\Squish for Java 6.2.0"
set SQUISH_SERVER_HOST="localhost"
set SQUISH_SERVER_PORT=4322
set TESTSUITE="C:\Users\training\suite_Framework"
set REPORTPATH="C:\Squish Reports\Framework"
set PYTHONPATH="C:\Users\training\Squish for Java 6.2.0\python"
cd %SQUISHPATH%\bin
squishrunner.exe --host %SQUISH_SERVER_HOST% --port %SQUISH_SERVER_PORT% --testsuite %TESTSUITE% --reportgen html,%REPORTPATH%
%REPORTPATH%\index.html
pause
