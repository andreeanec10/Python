#!/usr/bin/env python3

import csv

def read_employees(path):
    with open(path, 'r') as file_name:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(file_name, dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
        return employee_list

employee_list = read_employees("./by_department.csv")
print(employee_list)