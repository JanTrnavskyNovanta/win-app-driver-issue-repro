@ECHO off
TASKLIST | FINDSTR /i WinAppDriver.exe || start /B "" "C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
cd tested_app
pyinstaller __main__.spec -y
cd ..\tests
pytest
cd ..
echo Please press enter to make sure winappdriver is closed correctly (there can be an issue if it was run by this bat file)