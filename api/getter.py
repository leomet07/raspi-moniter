import os, csv

envloggerout = os.getenv("LOGGEROUT")
loggerout = envloggerout if envloggerout else '../data_logger'

def get_data():
    
    data = []
    with open(os.path.join(loggerout, 'data.csv'), 'r') as data_file:
        
        csv_reader = csv.reader(data_file)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            row = [None if x == "None" else x for x in row]
            data.append(row)
    
    return data


def get_loss():
    
    lossdict = {}
    with open(os.path.join(loggerout, 'data.csv'), 'r') as data_file:
        
        csv_reader = csv.reader(data_file) # Skip first line (The column names)

        next(csv_reader)
        
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            loss = row[-2]
            timestamp = row[-1]

            loss = None if loss == "None" else loss

            lossdict[timestamp] = loss
    
    return lossdict