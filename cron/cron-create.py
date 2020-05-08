from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python /full/path/to/testspeed.py /full/path/to/logs-dir server1 server2 ...', comment='Log connection speed')
job.minute.every(10)

cron.write()