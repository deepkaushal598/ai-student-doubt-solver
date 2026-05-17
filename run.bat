@echo off
echo.
echo ================================================
echo   AI Student Doubt Solver - Quick Start
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/3] Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo [2/3] Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo [2/3] Dependencies already installed
)

echo [3/3] Starting application...
echo.
echo ================================================
echo   Server is starting...
echo   Open: http://localhost:5000
echo ================================================
echo.

python Main.py
pause
