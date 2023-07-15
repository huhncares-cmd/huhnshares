# HuhnShares
## Setup
First, you need to git clone this repository. On Windows you might have to install git but you can also just download this repo from the website.
```
git clone https://github.com/huhncares-cmd/huhnshares.git
```
After that, you need to setup your virtual environment.
```
python3 -m venv venv
```
On Linux you might have to install python3-venv first. Simply type in this command:
```
sudo apt install python3-venv
```
On Windows you can jump into the environment like that on cmd:
```
venv\Scripts\activate.bat
```
And on Powershell:
```
venv\Scripts\Activate.ps1
```
On Linux it's a bit different because there are many shells out there. You can see what's right for you on the official website of Python (https://docs.python.org/3/library/venv.html), but for most users this command will work:
```
source venv/bin/activate
```
## Install requirements
When you are in your virtual environment, you can simply install all dependencies using this command:
```
pip3 install -r requirements.txt
```
## Run
You can run the site by executing main.py.
```
python3 main.py
```
## Finish
That's it. Your file sharing website will now run locally on port 1337. If you want to deploy this website you can take look at the docs. Tanks for using this project! Feedback on Twitter (https://twitter.com/huhncares) or GitHub is appreciated.
