import csv

# Save the output file url.txt in data folder
targetFileName='urls.csv'
targetFolder=os.getcwd()
# If the folder Does not exist it will be created
if os.path.exists(os.path.join( targetFolder,'data')):
    urlfile = os.path.join( targetFolder,'data',targetFileName)
else:
    os.makedirs(os.path.join( targetFolder,'data'))
    urlfile = os.path.join( targetFolder,'data',targetFileName)

with open(urlfile, 'rb') as f:
  data = list(csv.reader(f))


writer = csv.writer(open("/path/to/my/csv/file", 'w'))
for row in data:
    writer.writerow(row)