import sys
import os
import csv
import datetime
import speedtest

servers_amount = len(sys.argv) - 2
log_dir = sys.argv[1]

servers = []
for i in range(2, servers_amount):
	servers.append(ys.argv[i])


now = datetime.datetime.now()

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

download_speed = s.download() # in bits/second
upload_speed = s.upload() # in bits/second

download_speed_mbs = round(download_speed / 1000000, 2) # in megabits/second
upload_speed_mbs = round(upload_speed / 1000000, 2) # in megabits/second

date = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")
hour = now.strftime("%H") + ":" + now.strftime("%M")

time_header = "Time"
download_speed_header = "Download speed"
upload_speed_header = "Upload speed"

download_speed_str = str(download_speed_mbs)
upload_speed_str = str(upload_speed_mbs)

filename = log_dir + "/" + date + ".csv"

file_exists = os.path.isfile(filename)

with open(filename,"ab") as file_writer:

	fields=[time_header, download_speed_header, upload_speed_header]
	writer=csv.DictWriter(file_writer, fieldnames=fields)
	
	if not file_exists:
		writer.writeheader()
	
	writer.writerow({time_header:hour,download_speed_header:download_speed_str,upload_speed_header:upload_speed_str})