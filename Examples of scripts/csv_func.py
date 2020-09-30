import csv

#open file
#f = open("csv_file.txt")
#csv_f = csv.reader(f)
#for row in csv_f:
#   name, phone, role = row
#   print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()


#generate csv files
hosts = [["worksation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
