import csv
def read_csv_file():
    with open('C:\\CR\\dev\\rg.csv') as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        csvfile.seek(0)
        for row in reader:
            #print(row['rg'], row['vm'])
            resourceGroup=row['ResourceGroupName']
            vmName=row['VmName']
            stop_start_vm(resourceGroup,vmName)

def stop_start_vm(resourceGroup,vmName):
    print(resourceGroup)
    print(vmName)
read_csv_file()