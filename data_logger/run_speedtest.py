import os, sys, subprocess
import csv
from time import time

from datetime import datetime



expected = ["upload", "download", "loss", "utctime"]

filepath = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "data.csv")


def run_speedtest():
	output = str(subprocess.getoutput(["speedtest"])).strip().split("\n")

	download_raw = output[6]
	upload_raw = output[8]
	loss_raw = output[9]

	try:
		
		download_parsed = download_raw.strip().split(" ")
		download_parsed = float([i for i in download_parsed if i != ""][1])

		upload_parsed = upload_raw.strip().split(" ")
		upload_parsed = float([i for i in upload_parsed if i != ""][1])

		loss_parsed = loss_raw.strip().split(" ")
		loss_parsed = float([i for i in loss_parsed if i != ""][2][:3])
		
	except:
		print("An error occured, take a look at the output maybe?")
		print(download_raw)
		print(upload_raw)
		print(loss_raw)
		download_parsed = None
		upload_parsed = None
		loss_parsed = None

	currtime = str(datetime.utcnow())

	log_data(download_parsed, upload_parsed, loss_parsed, currtime)

def log_data(download, upload, loss, time):
	print(download, upload, loss, time)
	names = []
	
	

	if os.path.exists(filepath):
		with open(filepath, 'r') as csvfile:
			names = csvfile.readline().strip().split(",")
		
		if names != expected:
			print("Column names is not", str(expected) )
			create_new_datacsv()

	else:
		print("data.csv does not exist.")
		create_new_datacsv()
	
		
	with open(filepath, 'a') as csvfile:
		csvfile.write("\n" + str(download) + "," + str(upload) + "," + str(loss) + "," + str(time) )

	print("Data appended")

def create_new_datacsv():
	with open(filepath, "w") as file:
		file.write(",".join(expected))
	print("Created a new clean data.csv")
		

if __name__ == "__main__":
	run_speedtest()

