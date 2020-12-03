# Automated-Teams-join-meet using python

### Requirements:
***[Selenium Module](https://pypi.org/project/selenium/)***
```pip install selenium```

***[Schedule Module](https://pypi.org/project/schedule/)***
```pip install schedule``` (for schedule_join_meet.py file)

***[Chrome webdriver](https://chromedriver.chromium.org/downloads)*** Download the exact version of ChromeDriver which matches your chrome browser.

Paste chromedriver.exe in : ```C:\webdriver\bin\``` & set ```C:\webdriver\bin``` path in Environmental Variables.

### Setup:
Get the channel link:

![Image of Get Link](https://raw.githubusercontent.com/DurgaPrasadAG/Automated-Teams-join-meet/main/Image/GetLink.png)

#### Open join_meet.py file
1. Replace ***_\_link_\_*** with your channel link (line no: 20)
#### Example : ``` link = 'https://teams.microsoft.com/_?tenantId=abc'```
2. Replace ***email_id*** with your email id (line no: 28)
3. Replace ***_\_password_\_*** with your password (line no: 36)

#### Do the same for schedule_join_meet.py file. (line no: 24, 28 & 30)

#### If you want to schedule your meet, then run : ```pythonw schedule_join_meet.py``` You can close the terminal after typing this command and do your work. This will let the script to run in the background.

#### If you want to Direct join, then run : ```python join_meet.py```
