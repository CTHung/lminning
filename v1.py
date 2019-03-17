# -*- coding: cp950 -*-
import time
import re 

# 指定檔名
filename = 'lottery_u01.txt'
# 打開檔案
file = open (filename, 'r')
# 宣告一個紀錄陣列
# record[0] 表示第一行
# record[1] 表示第二行
record = []
number=['00','00','00','00','00','00','00']
record.append(number)

# 讀檔案
for line in file:
    # 換行符號去掉
    line = line.replace('\n', '')
    # 超過兩個空白 換成一個空白
    while '  ' in line:
        line = line.replace('  ', ' ')
    #print (line )
    # 以空白當分隔符號把數字讀進來 data
    data = line.split(' ')
    # data 的第一欄不需要 我們存第二欄到第八欄(1-7) 到number
    number = data[1:8]
    # 將 number 塞到 record 紀錄裡面
    record.append(number)


index_1 = 3
index_2 = 5
index_3 = 7

N1 = '06'
N2 = '08'
N3 = '09'

i = 0
success_list = []
while i < len(record):
    if i - index_1 < 0:
        i = i + 1
        continue
    if i - index_2 < 0:
        i = i + 1
        continue
    if i - index_3 < 0:
        i = i + 1
        continue

    if N1 in record[i-index_1]:
        if N2 in record[i-index_2]:
            if N3 in record[i-index_3]:
                success_list.append(i)
                print (i)
    i = i + 1


base_number = record[ success_list[len(success_list) -1] ]
serial = [0 ,0 ,0 ,0 ,0 ,0 ,0]

for record_id in reversed(success_list):
    print ('RID', record_id, record[record_id])
    for j in range(0, len(base_number)):
        if base_number[j] in record[record_id]:
            if serial[j] >= 0:
                serial[j] = serial[j]+1
        else:
            if serial[j] >= 0:
                serial[j] = serial[j] * -1
    #print ('S ', serial)

for j in range(0,len(serial)):
    print (base_number[j], ' has ', -1 * serial[j], 'times.')

    
    





