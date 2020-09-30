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

#DictWrite
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)

with open('by_department.csv', 'r') as by_department:
    reader = csv.DictReader(by_department)
    for row in reader:
        print(("{} coresponds to the user {}").format(row["username"], row["name"]))