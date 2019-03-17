# -*- coding: cp950 -*-

# run_03_xxxxx.bat �]��Ƥ��έp
# c:\Python27\python.exe stat_regular.py Lot3_output_01_02_03.txt Lot3_stat_r_01_02_03.txt
# c:\Python27\python.exe stat_regular.py Lot3_output_01_02_04.txt Lot3_stat_r_01_02_04.txt ...
# c:\Python27\python.exe stat_regular.py Lot3_output_01_02_05.txt Lot3_stat_r_01_02_49.txt




import time
import sys

if len(sys.argv) != 3:
    dumpline = 'c:\Python27\python.exe stat_inner.py input.txt output.txt'
    print (dumpline)
    quit()


filename = sys.argv[1]
file = open(filename, 'r')
outputfilename = sys.argv[2]
output = open(outputfilename, 'w')


freq = []
for i in range(0,21):
    array = [None] * 50
    for j in range (0, 50):
        array[j] = 0
    freq.append(array)

Bflag = False
Aflag = False
for line in file:
    # �ˬd�o�@��̭����S��  A B 
    #while c in line:
    #    if c == 'B':
    #        Bflag = True
    #    if c == 'A':
    #        Aflag = True
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
    fq = int(data[7])

    for i in range(0, 21):
        if fq == i:
            freq[i][id] = freq[i][id] + 1

dumpline = '#freq'
for i in range(1, 50):
    dumpline = dumpline + '\t' + str(i)
dumpline = dumpline + '\n'
output.write(dumpline)


for i in range(1, 21):
    dataflag = False
    for j in range(1, len(freq[i]) ):
        if freq[i][j] > 0:
           dataflag = True

    if dataflag == False:
        continue
    
    dumpline = '= ' + str(i)
    for j in range(1, len(freq[i]) ):
        dumpline = dumpline + '\t' + str(freq[i][j])

    dumpline = dumpline + '\n'
    output.write(dumpline)


# �̫�@�� �[�`
dumpline = '#SUM ' 
for j in range(1, len(freq[i]) ):
    sum = 0
    for i in range(1, 21):
        sum = sum + freq[i][j]
    dumpline = dumpline + '\t' + str(sum)

dumpline = dumpline + '\n'
output.write(dumpline)
    
        
