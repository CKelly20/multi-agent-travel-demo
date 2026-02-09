@echo off
echo Creating Python virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete. To activate the environment in future, run:
echo     CMD:        venv\Scripts\activate.bat
echo     PowerShell: .\venv\Scripts\Activate.ps1
echo.
echo Make sure to copy .env.sample to .env and fill in your API keys before running.
pause
