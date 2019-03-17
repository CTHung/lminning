# -*- coding: cp950 -*-
import time

# 副程式開始
# 給三個數字 跟 相對距離 找資料內所有符合的位置
def function(record, N1, N2, N3, relevent_1, relevent_2):
    i = 1
    success_list = []
    while i < len(record):
        if i - relevent_1 < 0:
            i = i + 1
            continue
        if i - relevent_2 < 0:
            i = i + 1
            continue
        if i - relevent_1 > len(record)-1:
            i = i + 1
            continue
        if i - relevent_2 > len(record)-1:
            i = i + 1
            continue

        #print (i, relevent_1, i - relevent_1, relevent_2, i - relevent_2, len(record))
        if N1 in record[i]:
            if N2 in record[i-relevent_1]:
                if N3 in record[i-relevent_2]:
                    success_list.append(i)
                    #print (i)
        i = i + 1

    return success_list
# 副程式結束






# 程式開始
# 指定檔名
filename = '3ST0002.txt'
# 連續出現次數
expected_counter = 6
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


# 距離
index_max = 400
# 號碼
N1 = '06'
N2 = '08'
N3 = '09'


outputfilename = '3S1output_' + N1 + '_' + N2 + '_' + N3 + '.txt'
output = open (outputfilename, 'w')

for relevent_1 in range( -index_max + 1, index_max):
    print(relevent_1)
    for relevent_2 in range( -index_max + 1, index_max):
        #print(relevent_1, relevent_2)
        pattern_list = function(record, N1, N2, N3, relevent_1, relevent_2)
        if len(pattern_list) < expected_counter:
            #print ('Ignore ', len(pattern_list) , ' < ' , expected_counter)
            continue
        #print ('R1 ', relevent_1, ' R2 ', relevent_2, ' len ', len(pattern_list))
        #print (pattern_list)
        for relevent_root in range(1, index_max+1):
            success_list = []
            index_1 = relevent_root
            index_2 = index_1 + relevent_1
            index_3 = index_1 + relevent_2
            dumpflag = False
            dupflag = False # 用來處理同一組有多個符合要求的號碼
            futureflag = False
            # 回算 index_1, index_2, index_3 是不是合理
            if index_2 <= index_max and index_3 <= index_max and index_2 > 0 and index_3 > 0:
                # 利用 pattern 相對位置 換算實際的絕對位置 successful list
                for j in range (0, len(pattern_list)):
                    success_list.append( pattern_list[j]+relevent_root )
                
                i = 0
                # 找出 baseline id 作過去的統計基準
                #print success_list, len(record) - 1
                for i in range(0, len(success_list)):
                    if success_list[i] < len(record):
                        base_line_id = success_list[i] 

                #print base_line_id
                base_number = record[base_line_id]
                serial = [0 ,0 ,0 ,0 ,0 ,0 ,0]

                # 資料統計 (資料內)
                for record_id in reversed(success_list):
                    if record_id <= base_line_id:
                        #print ('RID', record_id, record[record_id])
                        for j in range(0, len(base_number)):
                            if base_number[j] in record[record_id]:
                                if serial[j] >= 0:
                                    serial[j] = serial[j] + 1
                            else:
                                if serial[j] >= 0:
                                    serial[j] = serial[j] * -1
                j = 0            
                for i in range(0, len(serial)):
                    if serial[i] < 0:
                        serial[i] = serial[i] * -1
                    if serial[i] >= expected_counter:
                        j = j + 1
                if j == 0:
                    continue
                if j > 1:
                    dupflag = True
                        
                
                # 輸出未來次數 (資料外)
                record_id_future = []
                for record_id in reversed(success_list):
                    if record_id > base_line_id:
                        futureflag = True
                        record_id_future.append(record_id)
                        

                # 輸出
                for i in range(0, len(serial)):
                    if serial[i] >= expected_counter:
                        dumpline = str(index_3) + '\t' + N3 + '\t' + str(index_2) + '\t' +  N2 + '\t' + str(index_1) + '\t' + N1
                        dumpline = dumpline + '\t' + base_number[i] + '\t' + str(serial[i])
                        if dupflag:
                            dumpline = dumpline + '\tA'
                        j = serial[i]
                        if futureflag:
                            dumpline = dumpline + '\tB'
                            for id in record_id_future:
                                j = j + 1
                                dumpline = dumpline + '\t' + str(id) + '\t' + str(j)
                        #print (dumpline)
                        dumpline = dumpline + '\n'
                        output.write(dumpline)
                    
                                
            
                
                dumpflag = False
                dupflag = False
                futureflag = False
                




