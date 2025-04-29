# Institute-Wi-Fi-connection-Automation
This Python script automatically connects to the "ISM-Campus-Wi-Fi" network and logs in to the captive portal using your credentials. It's designed to run on Windows and is best scheduled using Task Scheduler to execute automatically after user login .


1)make a copy of the wifi_auto_login.py
2)replace the username and passwords with the actual usernames and passwords.
3)set-up a scheduler using the Task Scheduler application in Windows.

The below steps are for setting up the scheduler.

4)click on create task. (dont click on basic start!)
5)give a suitable name to the task.
6)check "Run only wehn user is logged on".
7)check "Run with highest privileges".
8)under "Triggers" section, click new, then select "At log on" from the drop down menu.
9)under "Actions" section, click new, then put the path of python.exe file under Program/script. It is generaly of the form: 
"C:\Users\<username>\AppData\Local\Programs\Python\Python313\python.exe" in windows. And put the absolute path of wifi_auto_login.py in the add arguments section.
10) under conditions section, make sure that the option: "Start the task only is computer is on AC power" is unchecked.
11) also make sure that the wifi option remains switched on at all times for the script to work!!
