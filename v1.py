# -*- coding: cp950 -*-
import time
import re 

# ���w�ɦW
filename = 'lottery_u01.txt'
# ���}�ɮ�
file = open (filename, 'r')
# �ŧi�@�Ӭ����}�C
# record[0] ��ܲĤ@��
# record[1] ��ܲĤG��
record = []
number=['00','00','00','00','00','00','00']
record.append(number)

# Ū�ɮ�
for line in file:
    # ����Ÿ��h��
    line = line.replace('\n', '')
    # �W�L��Ӫť� �����@�Ӫť�
    while '  ' in line:
        line = line.replace('  ', ' ')
    #print (line )
    # �H�ťշ���j�Ÿ���ƦrŪ�i�� data
    data = line.split(' ')
    # data ���Ĥ@�椣�ݭn �ڭ̦s�ĤG���ĤK��(1-7) ��number
    number = data[1:8]
    # �N number ��� record �����̭�
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

    
    





