# -*- coding: cp950 -*-

# run_02_A1_stat_future.bat �]�έp (��ƥ~) �p�U��G�X�վ��X���� (�C�q��s)
# c:\Python27\python.exe stat_future.py Lot3output_01_02_03.txt 2437 2450
# c:\Python27\python.exe stat_future.py Lot3output_01_02_04.txt 2437 2450
# c:\Python27\python.exe stat_future.py Lot3output_01_02_05.txt 2437 2450


import time
import sys

if len(sys.argv) != 4:
    dumpline = 'c:\Python27\python.exe stat_future.py input.txt start end'
    print (dumpline)
    filename = '3S1output_01_02_03.txt'
    file = open(filename, 'r')
    start_record = 2437
    end_record = 2445
    quit()
else:
    filename = sys.argv[1]
    file = open(filename, 'r')

    start_record = int (sys.argv[2])
    end_record = int (sys.argv[3])

outputfile_number = end_record - start_record + 1

table = {}

for i in range(start_record, end_record+1):
    array = []
    for j in range (0, 50):
        freq = []
        for k in range(0, 21):
            freq.append(0)
        #print (len(freq))
        array.append(freq)
    table[i] = array

#print len(table)
#print table

Bflag = False

for line in file:
    # �ˬd�o�@��̭����S�� B 
    for i in range(0 ,len(line)):
        if line[i] == 'B':
            Bflag = True
    # �S���ݨ�B ���L �B�z�U�@��
    if Bflag == False:
        continue
    Bflag = False
    # ����Ÿ��h��
    line = line.replace('\n', '')
    # tab �h��
    while '\t' in line:
        line = line.replace('\t', ' ')
    # �W�L��Ӫť� �����@�Ӫť�
    while '  ' in line:
        line = line.replace('  ', ' ')

    data = line.split(' ')
    id = int(data[6])
    fq = int(data[7]) + 1
    future_record_id = int (data[9])

    # �����d�򤧥~ ���Ҽ{ Ū�U�@��
    if future_record_id > end_record or future_record_id < start_record:
        continue
    #if future_record_id == 2437 and id == 2:
    #    print id, future_record_id, fq
    table[future_record_id][id][fq] = table[future_record_id][id][fq] + 1
    #if future_record_id == 2437 and id == 2:
    #    print 'N =', table[future_record_id][id][fq]
        

for key in table:
    outputfilename = str(key) + '_' + filename
    output = open(outputfilename, 'w')

    # �Ĥ@��
    dumpline = '# freq'
    for i in range(1, 50):
        dumpline = dumpline + '\t' + str(i).zfill(2)
    dumpline = dumpline + '\n'
    output.write(dumpline)

    # ��X���P�X�{�W�v
    for fq in range (0, 21):
        freqflag = False
        # �ˬd�O�_���X�{�W�v,�Y���s����X
        for id in range(1, 50):
            if table[key][id][fq] > 0:
               freqflag = True # ���έp��� �T�w��X
        if freqflag == False:
            continue
        # �Ĥ@��
        dumpline = '=' + str(fq)
        for id in range(1, 50):
            dumpline = dumpline + '\t' + str(table[key][id][fq])
        dumpline = dumpline + '\n'
        output.write(dumpline)

    # �̫�@�� �[�`
    dumpline = '#SUM=' 
    for id in range(1, 50):
        sum = 0 
        for fq in range (0, 21):
            sum = sum + table[key][id][fq]
        dumpline = dumpline + '\t' + str(sum)
    dumpline = dumpline + '\n'
    output.write(dumpline)
    
    output.close()

