## Usage:
written and testen in windows and powershell:
1) install python 3.6
2) install virtualenv: 'pip install virtualenv'
3) clone the repo
4) cd into the folder and make a virutalenv folder: 'virtualenv venv'
5) activate the virtual environment, '.\venv\Scripts\activate.ps1'
    you will get a (venv) prefix for you shell
6) install required packages: 'pip install -r .\requirements.txt'

ready to run the POC test!
AMF -> 'python poc_amf.py'

x) deactivate the environment 'deactivate'


##links:
https://www.python.org/downloads/release/python-366/

### reverse engineering help :)
https://media.blackhat.com/bh-us-12/Briefings/Carettoni/BH_US_12_Carettoni_AMF_Testing_Slides.pdf

### MIM tool
https://portswigger.net/burp
https://github.com/ikkisoft/blazer

### python libs
https://github.com/StdCarrot/Py3AMF
http://docs.python-requests.org/en/master/

### SQL 
https://cloudblogs.microsoft.com/sqlserver/2016/12/09/sql-server-python-whats-new/
https://github.com/mkleehammer/pyodbc/wiki
linux odbc drivers
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017

### Exchange using EWS
https://pypi.org/project/exchangelib/
https://github.com/ecederstrand/exchangelib