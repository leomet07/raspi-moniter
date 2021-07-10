import multiprocessing as mp
from multiprocessing import process
import os
import sys


def run_api(python_path):

    print("Api Thread starting")

    try:
        os.system(python_path + " " +  os.path.join("..", "api", "main.py"))
    except KeyboardInterrupt:
        pass

    print("Api Thread finishing")

def run_dashboard():

    print("Dashboard Thread starting")

    os.system("npm start --prefix " +  os.path.join("..", "dashboard"))

    print("Dashboard Thread finishing")
    
def run_data_logger(python_path):

    print("Data logger Thread starting")

    try:
        os.system(python_path + " " +  os.path.join("..", "data_logger", "main.py"))
    except KeyboardInterrupt:
        pass

    print("Dashboard Thread finishing")
    

if __name__ == "__main__":
    platform = sys.platform

    python_path = "python3"

    if platform.startswith("win"): 
        python_path = "python"


    api_process = mp.Process(target=run_api, args=(python_path, ))
    api_process.start()
    

    dashboard_process = mp.Process(target=run_dashboard)
    dashboard_process.start()

    
    logger_process = mp.Process(target=run_data_logger, args=(python_path, ))
    logger_process.start()
    
    
    logger_process.join()
    dashboard_process.join()
    api_process.join()