# Windows-Screentime-Scheduler
Lets us take a break from using the PC continuously


##Install

Clone this repository using the command

 `git clone https://github.com/akhileshkoti/Windows-Screentime-Scheduler.git`

or download the **[zip file](https://github.com/akhileshkoti/Windows-Screentime-Scheduler/archive/refs/heads/main.zip).**

##Usage

###Input the Schedule

- Run the **input-schedule.py** file that prompts to enter the no. of continuous working hours and no. of minutes of break.

### Running the script on startup
- Now create a shortcut to the **startup.bat** file and move that file to the windows startup folder.
-  To do that
   - Open Run dialogbox
   - Type shell:startup and press Enter
   - Now paste the startup.bat shortcut in this location
- The next time you boot your PC, the schedule starts running and you'll get your break at regular intervals of time.

### Terminating the Script

- If you want to stop the scheduled break then you have to run the kill code **kill.py**.
-  This will terminate the process initiated by **startup.bat**.
