# Speedtest Logger

Speedtest Logger is a small project that helps you monitor your Internet connection's speed, and store the information for future analysis.


# Prerequisites

- **speedtest-cli**  can be installed via command-line executing `pip install speedtest-cli`
- **python-crontab** can be installed via command-line executing `pip install python-crontab`

# Usage

## Manual run

In order to manually log the connection's speed you can run `speedtest-logger.py`. Parameters required for the run are an existing directory where the logs will be stored, and optional server IDs from where the script will choose the best (if empty, every server available will be considered). The command will look like one of these:

>`python speedtest-logger.py /relative/path/to/log/directory`  
>`python speedtest-logger.py /relative/path/to/log/directory 1234`  
>`python speedtest-logger.py /relative/path/to/log/directory 1234 5050`  
>`python speedtest-logger.py /relative/path/to/log/directory 1234 5050 999`  

Infinite server IDs can be added.

More information about the speedtest library [here](https://pypi.org/project/speedtest-cli/).
A list of available servers can be found [here](https://c.speedtest.net/speedtest-servers-static.php)

## Scheduling
The `cron` directory contains three extra Python scripts, that can be used to manage the cron job to schedule the logger run. 

`cron-create.py` needs to be overwritten, since it contains a dummy command. The real command should be like the manual run commands, but the path to the log directory needs to be absolute since cron jobs run elsewhere. It is set to run every 10 minutes, but that can easily be changed to the desired scheduling scheme. 

Once the settings have been adjusted, the cron job can be started by running `python testspeed-cron-create.py`. To check if the scheduling set was successful, you can run `python testspeed-cron-list.py`, and the created cron job should be listed on the terminal. To remove the job you can simply run `python testspeed-cron-remove.py`. 

More information about the scheduling library [here](https://pypi.org/project/python-crontab/).

# Output

The Speedtest Logger will generate, in the specified directory, a CSV file for each different date the script has been executed. Every file's name will be the date of the tests it contains (in yyyy-mm-dd format), and it will contain three columns (Time, Download speed, Upload speed). Both speed values will be expressed in mb/s. It will look like this:

`Time,Download speed,Upload speed`  
`17:00,5.32,2.37`  
`17:10,4.09,3.15`  
`17:20,4.89,2.58` 
