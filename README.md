# AmazonTestSpec
Appsfactory Challenge Tasks

**Technologies used:**
- python v3.10
- selenium v4.1.0
- behave framework v1.2.6
- PyCharm 2021.3 (Professional Edition)
- Chrome v96.0.4664.110

**Installation:**
1. Clone the **AmazonTestSpec** repository to your local computer. For example, C:\Git\AmazonTestSpec folder in Windows.
2. Install python
   1. Download the latest Python on the site **https://www.python.org/downloads/**
   2. For Windows OS - launch python-3.10.1-amd64.exe and set checkbox 'set HomePath'
   3. For Linux and Mac, please, follow the instruction on the official Python website.
3. Install selenium
   1. Run command prompt and perform the command: **pip install selenium**
4. Install behave framework
   1. Run command prompt and perform the command: **pip install behave**
5. Install Chrome browser v96.0.4664.110 or newer
   1. Use your computer’s browser to navigate to **https://www.google.com/chrome/** 
   2. For Windows OS - download and install **.exe** file
   3. For Linux and Mac, please, follow the instruction on the official Chrome website.

Now tests are ready for the run!

**Run the tests:**
1. Open command prompt.
2. Goto **<GitFolder>\AmazonTestSpec**, for example, C:\Git\AmazonTestSpec folder in Windows.
3. Perform command  **behave .\Features\AmazonTest.feature**

**Develop new tests:**
1. Open project in PyCharm
2. For easy to use install in PyCharm the following plugins:: 
- File->New Project Settings -> Python Interpreter, click install.
      1. selenium,
      2. behave

**Structure of the project:**
- **Driver** folder - includes ChromeWebDriver v.96 for different OS versions
- **Features** folder - includes Feature files with scenarios
- **Features/steps** folder - includes classes with Steps definitions for all pages and common class with initialization for Chrome
- **Features/steps/PageObjects** folder -includes classes with Page Objects for all pages
New Test can be added in Feature folder with extension **.feature**