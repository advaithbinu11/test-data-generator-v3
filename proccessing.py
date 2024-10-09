from testdata import generate_test
import json
import csv
import os
import logging
# Open and read the JSON file
def process(filename,output):
    logging.basicConfig(filename=output+'.log', level=logging.INFO)
    logging.info(output)
    with open(filename, 'r') as file:
        data = json.load(file)
    # Print the data
    fields = list(data['regex'].keys())
    logging.info(fields)
    # name of csv file
    filename = output
    # writing to csv file
    pdata=[]
    for j in range(data['tests']):
        mydict = {}
        for i in range(len(fields)):
            mydict[fields[i]] = (generate_test(data['regex'].get(fields[i]),output))
        logging.info(str(j)+" "+str(mydict))
        pdata.append(mydict)
    with open(filename+".csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(pdata)
        return os.path.abspath(filename)
        