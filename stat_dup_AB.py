# -*- coding: cp950 -*-

# run_????_stat_dup.bat 跑統計 ( 資料內 A )
# c:\Python27\python.exe stat_dup.py Lot3output_01_02_03.txt
# c:\Python27\python.exe stat_dup.py Lot3output_01_02_04.txt
# c:\Python27\python.exe stat_dup.py Lot3output_01_02_05.txt

import time
import sys

def printnumber(rid, ln, number, output):
    dumpline =  rid + '\t' + str(ln).zfill(2) + '\t' + str(number[0]).zfill(2)
    for i in range(1, len(number)):
        dumpline = dumpline + '\t' + str(number[i]).zfill(2)
    dumpline = dumpline + '\n'
    output.write(dumpline)

if len(sys.argv) != 3:
    dumpline = 'c:\Python27\python.exe stat_dup.py input.txt output.txt'
    print (dumpline)
    filename = '3S1output_01_02_03.txt'
    file = open(filename, 'r')
    outputfilename = 'dup_3S1output_01_02_03.txt'
    output = open(outputfilename, 'w')
    quit()
else:
    filename = sys.argv[1]
    file = open(filename, 'r')
    outputfilename = sys.argv[2]
    output = open(outputfilename, 'w')

printflag = False
number = []
index_0 = '-1'
index_1 = '-1'
index_2 = '-1'
index_3 = '-1'
index_4 = '-1'
index_5 = '-1'
old_record_ID = '-1'
old_last_number = -1
record_ID = '-1'
last_number = -1

for line in file:
    ABflag = False

    # 檢查這一行裡面有沒有 A
    for i in range(0 ,len(line)):
        if line[i:i+2] == 'AB': # 有 AB 就將計數器 + 1
            ABflag = True

    if ABflag == True:
        printflag = True
        # 換行符號去掉
        line = line.replace('\n', '')
        # tab 去掉
        while '\t' in line:
            line = line.replace('\t', ' ')
        # 超過兩個空白 換成一個空白
        while '  ' in line:
            line = line.replace('  ', ' ')

        data = line.split(' ')

        counter = 0
        if index_0 == data[0]:
            counter = counter + 1
        if index_1 == data[1]:
            counter = counter + 1
        if index_2 == data[2]:
            counter = counter + 1
        if index_3 == data[3]:
            counter = counter + 1
        if index_4 == data[4]:
            counter = counter + 1
        if index_5 == data[5]:
            counter = counter + 1

        old_record_ID = record_ID
        old_last_number = last_number
        record_ID = data[9]
        last_number = int(data[10])

        index_0 = data[0]
        index_1 = data[1]
        index_2 = data[2]
        index_3 = data[3]
        index_4 = data[4]
        index_5 = data[5]

        if len(number) != 0 and counter != 6:
            printnumber(old_record_ID, old_last_number, number, output)
            number = []

        id = int(data[6])
        # 將號碼記起來
        number.append(id)
        continue

    if len(number) != 0:
        printnumber(old_record_ID, old_last_number, number, output)
        number = []

if len(number) != 0:
    printnumber(old_record_ID, old_last_number, number, output)
