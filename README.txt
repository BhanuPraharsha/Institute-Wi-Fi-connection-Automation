**Instructions:**

1. Make a copy of `wifi_auto_login.py`.

2. Replace the placeholders for the username and password with your actual credentials.

3. Set up a scheduled task using the Task Scheduler application in Windows.

**To set up the task:**

4. Click on "Create Task" (do not click on "Basic Task").

5. Provide a suitable name for the task.

6. Check the box for "Run only when user is logged on."

7. Check the box for "Run with highest privileges."

8. In the "Triggers" section, click "New," then select "At log on" and "On workstation unlock" from the drop-down menu.

9. In the "Actions" section, click "New." Enter the path of the `python.exe` file under the "Program/script" field. It is generally located at:

   `C:\Users\<username>\AppData\Local\Programs\Python\Python313\python.exe`

   In the "Add arguments" section, provide the absolute path of `wifi_auto_login.py`.

10. Under the "Conditions" section, ensure that the option "Start the task only if the computer is on AC power" is unchecked.

Make sure that the Wi-Fi option remains switched on at all times for the script to work properly.

**Note:** This script is intended for connecting to the Wi-Fi network of IIT-ISM campus only. The name of the institute Wi-Fi may change, so update the Python script as needed.
