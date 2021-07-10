import os
import time
from dotenv import load_dotenv
load_dotenv()
from run_speedtest import run_speedtest
while True:
	run_speedtest()
	minutes =  os.getenv("SLEEPMIN") if os.getenv("SLEEPMIN") else 4
	time.sleep(60 * minutes)