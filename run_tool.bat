@echo off
chcp 65001 >nul
cd /d "%~dp0"
py -3 email_to_url.py
if errorlevel 1 (
    echo.
    echo Khong tim thay Python launcher "py".
    echo Hay cai Python 3 tu https://www.python.org/downloads/ va chon "Add Python to PATH".
    pause
)
