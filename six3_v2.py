# -*- coding: cp950 -*-

# ���X�m 2019.02.04
# �@�G1 �D�{�� six_v2 �� �I�k��� Edit with IDLE �s��
#     2 �۰ʰ��� �p�U
# �G�Grun_01_A0.bat run_01_B0.bat run_01_C0.bat run_01_D0.bat run_01_E0.bat �۰ʹB�� ( �ҥܦp�U ) 
# c:\Python27\python.exe six3_v2.py 01 02 03
# c:\Python27\python.exe six3_v2.py 01 02 04 .......
# c:\Python27\python.exe six3_v2.py 47 48 49
# �T�G800=180��()�B500=60��()�B400=40��()�B300=17��(6500)�B250=12��(4300)�B200=7��(2300) �Ѧҭ�                    
# �|�Gstat_future �]��ƥ~�έp�B stat_regular �]��Ƥ��έp�B stat_dup �]��� A �έp�Bstat_sum �C�ɲέp


import time
import sys


# �Ƶ{���}�l
# ���T�ӼƦr �� �۹�Z�� ���Ƥ��Ҧ��ŦX����m
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
# �Ƶ{������






# �{���}�l
# ���w�ɦW ( �}������� ) =====================
filename = 'run_Sixtery_u01.txt'
# �s��X�{���� ================================
expected_counter = 6
# ���Z ========================================
index_max = 200
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


# ���X
if len(sys.argv) != 4:
    dumpline = '��J: c:\Python27\python.exe six3_v2.py N1 N2 N3'
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


# ��X�W�� ====== 3S1output_ =====================================
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
            dupflag = False # �ΨӳB�z�P�@�զ��h�ӲŦX�n�D�����X
            futureflag = False
            base_line_id = -1
            # �^�� index_1, index_2, index_3 �O���O�X�z
            if index_2 <= index_max and index_3 <= index_max and index_2 > 0 and index_3 > 0:
                # �Q�� pattern �۹��m �����ڪ������m successful list
                for j in range (0, len(pattern_list)):
                    success_list.append( pattern_list[j]+relevent_root )
                
                i = 0
                # ��X baseline id �@�L�h���έp���
                #print success_list, len(record) - 1
                for i in range(0, len(success_list)):
                    if success_list[i] < len(record):
                        base_line_id = success_list[i] 

                #print base_line_id
                base_number = record[base_line_id][0:6]
                serial = [0 ,0 ,0 ,0 ,0 ,0 ]

                
                # ��Ʋέp (��Ƥ�)
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
                        
                
                # ��X���Ӧ��� (��ƥ~)
                record_id_future = []
                for record_id in success_list:
                    if record_id > base_line_id:
                        futureflag = True
                        record_id_future.append(record_id)
                        

                # ��X
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
                




