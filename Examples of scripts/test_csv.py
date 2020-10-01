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

def make_dict_of_frequency_I(list):
    dict = {}
    for elem in list:
        if elem not in dict:
            dict[elem] = 0
        dict[elem] += 1
    return dict

def make_dict_of_frequency_II(list):
    dict = {}
    for elem in set(list):
        dict[elem] = list.count(elem)
    return dict

def process_data(employee_list):
    department_list = []
    for employee in employee_list:
        department_list.append(employee["department"])
    department_data = make_dict_of_frequency_II(department_list)
    return department_data


employee_list = read_employees("./by_department.csv")
dictionary = process_data(employee_list)
print(dictionary)