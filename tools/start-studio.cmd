@echo off
rem Starts the ReliefNow Studio on this computer only (http://localhost:8765). Windows Task Scheduler
rem ("ReliefNow Studio") runs this automatically at sign-in; you can also double-click it.
rem Output goes to logs\studio.log.
cd /d "%~dp0.."
if not exist logs mkdir logs
echo [%date% %time%] starting the Studio >> logs\studio.log
call "%~dp0..\vedit.cmd" studio --no-open >> logs\studio.log 2>&1
exit /b %errorlevel%
