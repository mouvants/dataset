#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

fid = 'data1.csv'
output = fid[0:5] + '_comma.csv'
temp= []

with open(fid, newline='') as inputFile:
    reader = csv.reader(inputFile, delimiter=';', quotechar='|')
    for row in reader:
        temp.append(row)        

with open(output, 'w', newline='') as outputFile:
    for row in temp:
        writer = csv.writer(outputFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)
    