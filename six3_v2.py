# -*- coding: cp950 -*-

# 六合彩 2019.02.04
# 一：1 主程式 six_v2 檔 點右鍵選 Edit with IDLE 編輯
#     2 自動執行 如下
# 二：run_01_A0.bat run_01_B0.bat run_01_C0.bat run_01_D0.bat run_01_E0.bat 自動運行 ( 例示如下 ) 
# c:\Python27\python.exe six3_v2.py 01 02 03
# c:\Python27\python.exe six3_v2.py 01 02 04 .......
# c:\Python27\python.exe six3_v2.py 47 48 49
# 三：800=180分()、500=60分()、400=40分()、300=17分(6500)、250=12分(4300)、200=7分(2300) 參考值                    
# 四：stat_future 跑資料外統計、 stat_regular 跑資料內統計、 stat_dup 跑資料 A 統計、stat_sum 列檔統計


import time
import sys


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
# 指定檔名 ( 開獎資料檔 ) =====================
filename = 'run_Sixtery_u01.txt'
# 連續出現次數 ================================
expected_counter = 6
# 間距 ========================================
index_max = 200
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


# 號碼
if len(sys.argv) != 4:
    dumpline = '輸入: c:\Python27\python.exe six3_v2.py N1 N2 N3'
    print (dumpline)
    N1 = '01'
    N2 = '02'
    N3= '03'
    quit()
else:
    iN1 = sys.argv[1]
    iN2 = sys.argv[2]
    iN3 = sys.argv[3]
    N1 = iN1.zfill(2)
    N2 = iN2.zfill(2)
    N3 = iN3.zfill(2)
    dumpline = 'N1=' + N1 + ' N2=' + N2 + ' N3=' + N3
    print (dumpline)


# 輸出名稱 ====== 3S1output_ =====================================
outputfilename = 'Six3_output_' + N1 + '_' + N2 + '_' + N3 + '.txt'
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
            base_line_id = -1
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
                base_number = record[base_line_id][0:6]
                serial = [0 ,0 ,0 ,0 ,0 ,0 ]

                
                # 資料統計 (資料內)
                for record_id in reversed(success_list):
                    if record_id <= base_line_id:
                        #print ('RID', record_id, record[record_id])
                        for j in range(0, len(base_number)):
                            if base_number[j] in record[record_id][0:6]:
                                #if index_1 == 359 and index_2 == 18 and index_3 == 99:
                                #    print base_line_id, record_id, base_number, index_1, index_2, index_3
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
                for record_id in success_list:
                    if record_id > base_line_id:
                        futureflag = True
                        record_id_future.append(record_id)
                        

                # 輸出
                for i in range(0, len(serial)):
                    if serial[i] >= expected_counter:
                        dumpline = str(index_3) + '\t' + N3 + '\t' + str(index_2) + '\t' +  N2 + '\t' + str(index_1) + '\t' + N1
                        dumpline = dumpline + '\t' + base_number[i] + '\t' + str(serial[i])
                        if dupflag:
                            if futureflag:
                                dumpline = dumpline + '\tAB'
                            else:
                                dumpline = dumpline + '\tA'
                        else:
                            if futureflag:
                                dumpline = dumpline + '\tB'

                        if futureflag:
                            j = serial[i]
                            for id in record_id_future:
                                j = j + 1
                                dumpline = dumpline + '\t' + str(id) + '\t' + str(j)
                            
                        #print (dumpline)
                        dumpline = dumpline + '\n'
                        output.write(dumpline)
                    
                                
            
                
                dumpflag = False
                dupflag = False
                futureflag = False
                




