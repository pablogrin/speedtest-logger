from crontab import CronTab

cron = CronTab(user=True)

jobs = cron.find_comment('Log connection speed')
cron.remove(jobs)

jobs = cron.find_comment('Log connection speed')

for job in jobs:
	print(job)

cron.write()