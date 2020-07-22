# Website-Blocker
This application will block the websites mentioned for a specific time frame.
There is a file named main.pyw which is runs in background, when double clicked, this will restrict the user to visit the mentioned websites in the main.pyw file within the given time frame by blocking the websites and redirecting the connection request to 127.0.0.1. It works by updating the hosts file present in etc directory.
The code will work both on UNIX and Windows platform. For sake of simplicity we are mentioning steps to make it run automatically at startup on WINDOWS. 
You need to follow steps mentioned below:
Step 1: Go to Windows Task Scheduler.
Step 2: Double Click 'Create Task', on right pane.
Step 3: On Create Task Window, mention a name to the program (say "My Web Blocker"), check 'Run with Highest Privileges' this is done to get privileges to access hosts file.
Step 4: Go to Trigger, Click on New.
Step 5: On New Window, Selct 'At Startup' and click on OK.
Step 6: Now go to 'Actions' tab and click on 'New".
Step 7: Provide full path to your pwy.exe (which must be same as python.exe) in program section.
Step 8 : In Add arguments section, provide complete path to main.py (with double quotes). For example, "C:\users\rvrishav\Desktop\main.pyw".
Step 9: Click on OK. And the click on OK, again to close 'Create Task Window'.
Step 10: In the programs, running you could see your program in the list. To run it now select it, click on 'Run'. 
Step 11: It will start working as you reboot your PC.
