# -*- coding: cp950 -*-

# run_05_sum.bat 跑資料 統計加總
# c:\Python27\python.exe
# stat_sum.py 本主程式
# sum_file_list.txt 統計範圍 (檔案) 列表
   # 2437_Lot3_output_01_02_03.txt
   # 2437_Lot3_output_01_02_04.txt .......
   # 2437_Lot3_output_01_02_49.txt
# sum.txt 統計成果

import time
import sys

if len(sys.argv) != 2:
    dumpline = 'c:\Python27\python.exe stat_sum.py sum_file_list.txt'
    filelistname = 'sum_file_list.txt'
    print (dumpline)
    quit()
else:
    filelistname = sys.argv[1]

filelist = open(filelistname, 'r')
#############################################
# outputfilename = 'sum.txt' 
outputfilename = 'sum_' + filelistname
#############################################
output = open(outputfilename, 'w')

#print head
dumpline = '#Freq'
for i in range(1, 50):
    dumpline = dumpline + '\t' + str(i)
dumpline = dumpline + '\n'   
output.write(dumpline)

s = []
for i in range(0,21):
    v = []
    for j in range(0,50):
        v.append(0)
    s.append(v)

for filename in filelist:
    file = open (filename.strip(), 'r')
    for line in file:
        # 跳過 # 開頭
        if line[0] == '#':
            continue
        line = line.replace('\n', '')
        # tab 去掉
        while '\t' in line:
            line = line.replace('\t', ' ')
        # 超過兩個空白 換成一個空白
        while '  ' in line:
            line = line.replace('  ', ' ')

        data = line.split(' ')

        # 檢查資料是不是 = 開頭
        if data[0][0] != '=':
            print ('Data head is not =')
            quit()

        serial = int(data[0][1:])
        number = []
        for i in range(1,50):
            s[serial][i] = s[serial][i] + int(data[i])
            

sum = []
for i in range(0,50):
    sum.append(0)

for i in range(1, 21):
    counter = 0
    for v in s[i]:
        counter = counter + v
    if counter == 0:
        continue
    
    dumpline = '=' + str(i)
    for j in range(1, len(s[i])):
        dumpline = dumpline + '\t' + str(s[i][j])
        sum[j] = sum[j] + s[i][j]
    dumpline = dumpline + '\n'
    output.write(dumpline)

#print tail
dumpline = '#SUM'
for i in range(1, 50):
    dumpline = dumpline + '\t' + str(sum[i])
dumpline = dumpline + '\n'   
output.write(dumpline)



    
output.close()
        
