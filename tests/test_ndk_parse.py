import sys; sys.path.append('../')
from gcmt_utils.ndk_parser import *

ndk_test_1 = '''
PDE  2005/01/01 01:20:05.4  13.78  -88.78 193.1 5.0 0.0 EL SALVADOR             
C200501010120A   B:  4    4  40 S: 27   33  50 M:  0    0   0 CMT: 1 TRIHD:  0.6
CENTROID:     -0.3 0.9  13.76 0.06  -89.08 0.09 162.8 12.5 FREE S-20050322125201
23  0.838 0.201 -0.005 0.231 -0.833 0.270  1.050 0.121 -0.369 0.161  0.044 0.240
V10   1.581 56  12  -0.537 23 140  -1.044 24 241   1.312   9 29  142 133 72   66
'''

ndk_test_2 = '''
PDE  2005/01/01 01:20:05.4  13.78  -88.78 193.1 5.0 0.0 EL SALVADOR             
C200501010120A   B:  4    4  40 S: 27   33  50 M:  0    0   0 CMT: 1 TRIHD:  0.6
CENTROID:     -0.3 0.9  13.76 0.06  -89.08 0.09 162.8 12.5 FREE S-20050322125201
23  0.838 0.201 -0.005 0.231 -0.833 0.270  1.050 0.121 -0.369 0.161  0.044 0.240
V10   1.581 56  12  -0.537 23 140  -1.044 24 241   1.312   9 29  142 133 72   66
PDE  2005/01/01 01:42:24.9   7.29   93.92  30.0 5.1 0.0 NICOBAR ISLANDS, INDIA R
C200501010142A   B: 17   27  40 S: 41   58  50 M:  0    0   0 CMT: 1 TRIHD:  0.7
CENTROID:     -1.1 0.8   7.24 0.04   93.96 0.04  12.0  0.0 BDY  S-20050322125628
23 -1.310 0.212  2.320 0.166 -1.010 0.241  0.013 0.535 -2.570 0.668  1.780 0.151
V10   3.376 16 149   0.611 43  44  -3.987 43 254   3.681 282 48  -23  28 73 -136
'''


test_ndk_file = './test_data/jan15.ndk'

eq_list_test_1 = parse_ndk_string(ndk_test_1)
eq_list_test_2 = parse_ndk_string(ndk_test_2)

eq_list_file_1 = parse_ndk_file(test_ndk_file)

el = eq_list_test_1
e1 = eq_list_file_1[0]
