from django import template
import math
register = template.Library()

import decimal
a = decimal.Decimal("8.833333333339")
# print(round(a,2))

array = [['0.00384615', '0.00564972', '0.0057971', '0.0057971', '0.00653595', '0.00772201', '0.00881057', '0.0108303', '0.0131579', '0.0131579', '0.012605', '0.0117647', '0.0117647', '0.0117647', '0.0117647', '0.0208333', '0.0232558', '0.030303', '0.0277778', '0.025641', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0.00384615', '0.00653595', '0.00653595', '0.00653595', '0.00653595', '0.00772201', '0.0108303', '0.011811', '0.012605', '0.012605', '0.012605', '0.0108696', '0.0117647', '0.0117647', '0.015625', '0.0208333', '0.0232558', '0.025641', '0.0277778', '0.0277778', '0.025641', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0.00384615', '0.00653595', '0.00735294', '0.00724638', '0.00724638', '0.0116959', '0.011811', '0.011811', '0.011811', '0.011811', '0.0105263', '0.0105263', '0.0108696', '0.0120482', '0.015625', '0.0172414', '0.0222222', '0.0232558', '0.0277778', '0.0277778', '0.0277778', '0.0277778', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0.00735294', '0.00909091', '0.00940439', '0.0116959', '0.0116959', '0.0116959', '0.011811', '0.0106383', '0.0105263', '0.0105263', '0.0105263', '0.0106383', '0.015625', '0.0172414', '0.0172414', '0.0172414', '0.0222222', '0.0277778', '0.0277778', '0.0333333', '0.0425532', '0.05', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0.00847458', '0.00909091', '0.00940439', '0.00995025', '0.0116959', '0.00966184', '0.00966184', '0.0105263', '0.0105263', '0.0106383', '0.0106383', '0.0125', '0.015625', '0.0172414', '0.0172414', '0.0208333', '0.0222222', '0.0277778', '0.0333333', '0.0425532', '0.0625', '0.0625', '0.05', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0.00909091', '0.00909091', '0.00647249', '0.00647249', '0.00831025', '0.00947867', '0.00947867', '0.0106383', '0.0110497', '0.0121951', '0.0125', '0.0181818', '0.0181818', '0.02', '0.0240964', '0.0277778', '0.0333333', '0.037037', '0.0425532', '0.0625', '0.0625', '0.05', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0.00600601', '0.00609756', '0.00609756', '0.00609756', '0.00729927', '0.00831025', '0.00947867', '0.0111732', '0.0120968', '0.0122699', '0.0125', '0.0181818', '0.02', '0.0240964', '0.0277778', '0.0307692', '0.0333333', '0.037037', '0.0425532', '0.0625', '0.0625', '0.0555556', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0.00600601', '0.00600601', '0.00609756', '0.00609756', '0.00831025', '0.00852273', '0.0111732', '0.0120968', '0.0122699', '0.0125', '0.0125', '0.0181818', '0.0232558', '0.0240964', '0.0277778', '0.0307692', '0.0333333', '0.0425532', '0.0487805', '0.0625', '0.0625', '0.0555556', '0.05', '0', '0', '0', '0', '0.0588235', '0.0588235', '0', '0', '0', '0', '0', '0', '0'], ['0', '0.0049505', '0.00600601', '0.00852273', '0.00852273', '0.00842697', '0.00852273', '0.00852273', '0.0120968', '0.0120968', '0.0125', '0.0125', '0.0180723', '0.0232558', '0.0232558', '0.0240964', '0.0277778', '0.0307692', '0.0344828', '0.0487805', '0.0487805', '0.0535714', '0.0769231', '0.0769231', '0.0555556', '0.0555556', '0.0555556', '0.0588235', '0.0588235', '0.0588235', '0.0588235', '0.0588235', '0', '0', '0', '0', '0', '0'], ['0', '0.0052356', '0.00854701', '0.00854701', '0.00854701', '0.00852273', '0.00852273', '0.00852273', '0.0120968', '0.0144404', '0.0157729', '0.0166113', '0.0180723', '0.0232558', '0.0232558', '0.0240964', '0.0333333', '0.0344828', '0.0487805', '0.0487805', '0.0487805', '0.0535714', '0.0769231', '0.0769231', '0.0769231', '0.0666667', '0.0666667', '0.0666667', '0.0625', '0.0588235', '0.0588235', '0.0588235', '0', '0', '0', '0', '0', '0'], ['0', '0.0052356', '0.00854701', '0.00854701', '0.00854701', '0.00854701', '0.00852273', '0.00884956', '0.0140845', '0.0157729', '0.0164835', '0.0166113', '0.0198675', '0.0232558', '0.0245902', '0.0348259', '0.0413793', '0.0526316', '0.0535714', '0.0487805', '0.0487805', '0.0535714', '0.0769231', '0.0857143', '0.0857143', '0.0769231', '0.0666667', '0.0666667', '0.0666667', '0.0666667', '0.0833333', '0.0833333', '0.1', '0', '0', '0', '0', '0'], ['0', '0.00854701', '0.00854701', '0.00854701', '0.00854701', '0.00884956', '0.00952381', '0.01', '0.0140845', '0.0157729', '0.0166113', '0.0166113', '0.0201005', '0.0245902', '0.0348259', '0.0413793', '0.0526316', '0.0543478', '0.0597015', '0.0576923', '0.0576923', '0.0597015', '0.0857143', '0.0869565', '0.0909091', '0.0909091', '0.0909091', '0.0833333', '0.0833333', '0.0833333', '0.1', '0.1', '0.1', '0.1', '0', '0', '0', '0'], ['0', '0.00854701', '0.00854701', '0.00854701', '0.00854701', '0.00952381', '0.01', '0.0140187', '0.0140845', '0.0164835', '0.0166113', '0.0201005', '0.0257732', '0.0290909', '0.0357143', '0.0422535', '0.0543478', '0.0597015', '0.0597015', '0.0597015', '0.0597015', '0.0714286', '0.0869565', '0.0909091', '0.0909091', '0.105263', '0.105263', '0.117647', '0.117647', '0.1', '0.1', '0.111111', '0.111111', '0.111111', '0', '0', '0', '0'], ['0.00442478', '0.00854701', '0.00854701', '0.00854701', '0.00854701', '0.01', '0.013587', '0.0140845', '0.0152284', '0.019337', '0.0242424', '0.0272727', '0.0290909', '0.0344828', '0.0368664', '0.0422535', '0.0543478', '0.0597015', '0.0597015', '0.0677966', '0.0714286', '0.0714286', '0.0869565', '0.105263', '0.125', '0.136364', '0.142857', '0.142857', '0.142857', '0.166667', '0.1875', '0.2', '0.2', '0.2', '0.153846', '0', '0', '0'], ['0.00925926', '0.010929', '0.00925926', '0.00925926', '0.00974026', '0.013587', '0.0140845', '0.0152284', '0.019337', '0.0242424', '0.0272727', '0.028169', '0.0321101', '0.0348259', '0.0368664', '0.0438596', '0.0529801', '0.0597015', '0.0689655', '0.0705882', '0.0714286', '0.0769231', '0.0909091', '0.116279', '0.125', '0.142857', '0.142857', '0.142857', '0.166667', '0.1875', '0.2', '0.222222', '0.2', '0.2', '0.2', '0', '0', '0'], ['0.011236', '0.011236', '0.011236', '0.010929', '0.0124688', '0.0152284', '0.0152284', '0.019337', '0.020202', '0.0255682', '0.028169', '0.028169', '0.0321101', '0.0357143', '0.0376569', '0.0473373', '0.0529801', '0.0689655', '0.0705882', '0.0769231', '0.0779221', '0.0909091', '0.111111', '0.116279', '0.125', '0.136364', '0.15', '0.166667', '0.166667', '0.166667', '0.222222', '0.25', '0.222222', '0.2', '0.142857', '0', '0', '0.142857'], ['0.010929', '0.011236', '0.011236', '0.0124688', '0.0152284', '0.0159236', '0.0178571', '0.020202', '0.0243309', '0.0272727', '0.028169', '0.0289855', '0.0321101', '0.0376569', '0.0473373', '0.0529801', '0.0670732', '0.0705882', '0.08', '0.0833333', '0.0978261', '0.0980392', '0.111111', '0.111111', '0.116279', '0.136364', '0.15', '0.166667', '0.166667', '0.166667', '0.222222', '0.25', '0.25', '0.2', '0.142857', '0.142857', '0.142857', '0.2'], ['0.010929', '0.011236', '0.011236', '0.0136986', '0.0159236', '0.0177515', '0.0183246', '0.020202', '0.0255682', '0.028169', '0.0289855', '0.0300546', '0.0376569', '0.0436508', '0.048', '0.054878', '0.0705882', '0.08', '0.0978261', '0.0980392', '0.0980392', '0.0980392', '0.111111', '0.111111', '0.116279', '0.136364', '0.15', '0.166667', '0.166667', '0.166667', '0.222222', '0.25', '0.25', '0.2', '0.142857', '0.142857', '0.142857', '0.25'], ['0.010929', '0.010929', '0.011236', '0.0136986', '0.0159236', '0.0177515', '0.0183246', '0.020202', '0.0272727', '0.0289855', '0.0300546', '0.0376569', '0.0436508', '0.0467836', '0.054878', '0.0643275', '0.0720721', '0.0978261', '0.102564', '0.102564', '0.102564', '0.102941', '0.111111', '0.116279', '0.136364', '0.15', '0.166667', '0.166667', '0.166667', '0.181818', '0.222222', '0.272727', '0.272727', '0.25', '0.2', '0.142857', '0.2', '0.25'], ['0.010929', '0.011236', '0.0114943', '0.0140845', '0.0159091', '0.0177515', '0.0184211', '0.0209524', '0.0272727', '0.0300546', '0.0376569', '0.0433604', '0.0467836', '0.0492424', '0.0611511', '0.0714286', '0.077381', '0.102564', '0.102941', '0.102941', '0.111111', '0.131868', '0.134615', '0.145833', '0.170213', '0.1875', '0.1875', '0.1875', '0.181818', '0.181818', '0.222222', '0.272727', '0.285714', '0.285714', '0.25', '0.25', '0.25', '0.25'], ['0.0114943', '0.0114943', '0.0114943', '0.0140845', '0.0159091', '0.0184211', '0.0209205', '0.025', '0.0296736', '0.037037', '0.0410256', '0.046875', '0.0492424', '0.0611511', '0.0704225', '0.077381', '0.0859375', '0.102941', '0.104545', '0.111111', '0.131868', '0.134615', '0.169492', '0.180328', '0.190476', '0.208333', '0.190476', '0.190476', '0.1875', '0.210526', '0.222222', '0.272727', '0.272727', '0.285714', '0.25', '0.25', '0.25', '0.25'], ['0.0133333', '0.0114943', '0.0133333', '0.0140845', '0.0184211', '0.0207792', '0.022', '0.0258065', '0.033195', '0.0410256', '0.046875', '0.0491803', '0.0611511', '0.0704225', '0.077381', '0.078853', '0.0859375', '0.104545', '0.111111', '0.130137', '0.131868', '0.169492', '0.180328', '0.181818', '0.208333', '0.208333', '0.208333', '0.210526', '0.210526', '0.222222', '0.222222', '0.272727', '0.3', '0.3', '0.285714', '0.285714', '0.285714', '0.285714'], ['0.0133333', '0.0133333', '0.0140845', '0.0144928', '0.0184211', '0.0209205', '0.0230126', '0.0271399', '0.0397196', '0.046875', '0.046875', '0.0491803', '0.0704225', '0.0774648', '0.078853', '0.0859375', '0.104545', '0.111702', '0.130137', '0.130137', '0.141026', '0.169492', '0.180328', '0.206349', '0.208333', '0.208333', '0.208333', '0.210526', '0.210526', '0.222222', '0.25', '0.333333', '0.333333', '0.333333', '0.333333', '0.285714', '0.285714', '0.333333'], ['0.0133333', '0.0144928', '0.0144928', '0.0147059', '0.0207792', '0.0230126', '0.025974', '0.028436', '0.0439367', '0.046875', '0.0485437', '0.0537313', '0.0774648', '0.0875332', '0.0933852', '0.104545', '0.111702', '0.130137', '0.130137', '0.141026', '0.169492', '0.180328', '0.206349', '0.208333', '0.208333', '0.208333', '0.210526', '0.222222', '0.222222', '0.25', '0.333333', '0.333333', '0.333333', '0.333333', '0.3', '0.285714', '0.285714', '0.333333'], ['0.0170455', '0.0170455', '0.0149626', '0.0207792', '0.0231481', '0.025974', '0.0271399', '0.028436', '0.0439367', '0.0485437', '0.0485437', '0.0537313', '0.0875332', '0.0933852', '0.104545', '0.110294', '0.119048', '0.130137', '0.141026', '0.152174', '0.193182', '0.206349', '0.211538', '0.211538', '0.211538', '0.220779', '0.243902', '0.222222', '0.25', '0.307692', '0.357143', '0.357143', '0.333333', '0.3', '0.25', '0.25', '0.285714', '0.333333'], ['0.0186335', '0.0186335', '0.0217391', '0.0251256', '0.0268817', '0.0271399', '0.0274841', '0.0313725', '0.0462107', '0.0485437', '0.0519126', '0.0544747', '0.0900322', '0.102941', '0.107784', '0.111702', '0.129496', '0.141026', '0.151316', '0.193182', '0.206349', '0.211538', '0.217949', '0.22', '0.220779', '0.25', '0.25', '0.25', '0.25', '0.307692', '0.357143', '0.357143', '0.333333', '0.285714', '0.25', '0.25', '0.285714', '0.333333'], ['0.023622', '0.023622', '0.0251256', '0.0268817', '0.0268817', '0.0272374', '0.0313725', '0.0378947', '0.0462107', '0.0508475', '0.0541176', '0.0802752', '0.0900322', '0.10566', '0.111111', '0.129496', '0.134529', '0.151316', '0.161905', '0.206349', '0.211538', '0.217949', '0.22', '0.220779', '0.244898', '0.25', '0.25', '0.25', '0.25', '0.307692', '0.357143', '0.357143', '0.333333', '0.285714', '0.25', '0.25', '0.285714', '0.333333'], ['0.025', '0.025', '0.0251256', '0.0268817', '0.0268817', '0.0272374', '0.0327022', '0.0378947', '0.0462107', '0.0541176', '0.0563063', '0.0811688', '0.0900322', '0.111111', '0.12749', '0.134529', '0.151316', '0.159363', '0.176829', '0.206349', '0.215385', '0.22', '0.220779', '0.244898', '0.277778', '0.277778', '0.25', '0.25', '0.307692', '0.333333', '0.333333', '0.333333', '0.333333', '0.307692', '0.285714', '0.285714', '0.333333', '0.333333'], ['0.023622', '0.023622', '0.0243902', '0.0255814', '0.0268817', '0.0279503', '0.0342857', '0.0397237', '0.047259', '0.0544747', '0.058209', '0.0877193', '0.0976331', '0.123123', '0.134529', '0.142857', '0.159363', '0.168831', '0.176829', '0.215054', '0.217949', '0.227848', '0.244898', '0.277778', '0.277778', '0.278689', '0.282609', '0.304348', '0.333333', '0.333333', '0.333333', '0.333333', '0.307692', '0.307692', '0.307692', '0.333333', '0.333333', '0.375'], ['0.0224719', '0.0224719', '0.0243902', '0.0244499', '0.0272374', '0.0342466', '0.0363636', '0.043364', '0.0490998', '0.0580524', '0.0650096', '0.0976331', '0.123123', '0.12749', '0.141148', '0.152', '0.164336', '0.175926', '0.185629', '0.217949', '0.230769', '0.243243', '0.25641', '0.277778', '0.278689', '0.282609', '0.304348', '0.342105', '0.347826', '0.347826', '0.333333', '0.318182', '0.307692', '0.333333', '0.363636', '0.375', '0.375', '0.5'], ['0.0224719', '0.023622', '0.0244499', '0.0244499', '0.0279503', '0.0346715', '0.0424077', '0.047619', '0.056', '0.0625', '0.075643', '0.108696', '0.127219', '0.141148', '0.145985', '0.164336', '0.175926', '0.185629', '0.235772', '0.235772', '0.243243', '0.25', '0.275862', '0.278689', '0.278689', '0.282609', '0.333333', '0.342105', '0.347826', '0.347826', '0.318182', '0.318182', '0.318182', '0.363636', '0.375', '0.5', '0.5', '0.5'], ['0.0269058', '0.0269058', '0.0269058', '0.0269058', '0.0297398', '0.0388693', '0.043364', '0.0509091', '0.058209', '0.0639687', '0.0874233', '0.112392', '0.129264', '0.145985', '0.164336', '0.173285', '0.185629', '0.235772', '0.238683', '0.25', '0.253846', '0.25641', '0.278689', '0.278689', '0.282609', '0.333333', '0.342105', '0.347826', '0.347826', '0.347826', '0.318182', '0.318182', '0.318182', '0.363636', '0.5', '0.5', '0.555556', '0.6'], ['0.029304', '0.0269058', '0.0269058', '0.0277136', '0.0303514', '0.0394511', '0.0467422', '0.056', '0.0625', '0.0802676', '0.0966387', '0.112392', '0.129264', '0.15', '0.173285', '0.177515', '0.21875', '0.238683', '0.253846', '0.254902', '0.25641', '0.304636', '0.308511', '0.313953', '0.333333', '0.342105', '0.372549', '0.372549', '0.37037', '0.347826', '0.347826', '0.318182', '0.352941', '0.5', '0.5', '0.538462', '0.6', '0.6'], ['0.029304', '0.0277136', '0.0277136', '0.0277136', '0.0371517', '0.0394511', '0.0467422', '0.0578871', '0.0796089', '0.0874233', '0.106796', '0.121951', '0.129264', '0.15', '0.175966', '0.186544', '0.22549', '0.238683', '0.254902', '0.2625', '0.304636', '0.308511', '0.313953', '0.318182', '0.352941', '0.372549', '0.386364', '0.386364', '0.371429', '0.37037', '0.352941', '0.352941', '0.444444', '0.5', '0.533333', '0.555556', '0.555556', '0.6'], ['0.027907', '0.0277136', '0.0277136', '0.0277136', '0.0371517', '0.0446602', '0.0577778', '0.0632258', '0.0796089', '0.0941828', '0.106796', '0.124343', '0.133949', '0.160656', '0.175966', '0.20059', '0.22549', '0.241379', '0.2625', '0.298137', '0.308511', '0.310811', '0.318182', '0.352941', '0.372549', '0.372549', '0.386364', '0.386364', '0.386364', '0.371429', '0.428571', '0.444444', '0.5', '0.5', '0.538462', '0.555556', '0.555556', '0.666667'], ['0.027907', '0.027907', '0.0277136', '0.0371517', '0.0434783', '0.0531136', '0.0614973', '0.0645161', '0.0802676', '0.0941828', '0.117537', '0.128244', '0.137285', '0.161232', '0.175966', '0.217391', '0.22549', '0.247863', '0.292517', '0.308511', '0.309677', '0.329114', '0.336842', '0.372549', '0.372549', '0.386364', '0.386364', '0.386364', '0.386364', '0.428571', '0.444444', '0.473684', '0.5', '0.533333', '0.541667', '0.555556', '0.625', '0.666667'], ['0.0281124', '0.0281124', '0.0371517', '0.0434783', '0.0448065', '0.0531136', '0.0632258', '0.066313', '0.0860215', '0.103208', '0.128244', '0.136289', '0.160656', '0.174672', '0.199195', '0.219373', '0.243902', '0.278846', '0.304636', '0.309677', '0.329114', '0.333333', '0.342593', '0.375', '0.395062', '0.4', '0.416667', '0.416667', '0.428571', '0.428571', '0.454545', '0.473684', '0.5', '0.533333', '0.555556', '0.6', '0.625', '0.666667'], ['0.0326087', '0.037037', '0.0434783', '0.0448065', '0.0458716', '0.0529595', '0.0658307', '0.0714286', '0.0860215', '0.103208', '0.136289', '0.158019', '0.169903', '0.188889', '0.217391', '0.236686', '0.253275', '0.292517', '0.309677', '0.329114', '0.333333', '0.342593', '0.372549', '0.395062', '0.4', '0.416667', '0.416667', '0.428571', '0.428571', '0.428571', '0.444444', '0.473684', '0.5', '0.533333', '0.6', '0.6', '0.625', '0.666667'], ['0.037037', '0.037037', '0.0434783', '0.0448065', '0.0504854', '0.0529595', '0.0667506', '0.0757381', '0.0899855', '0.112857', '0.138024', '0.161232', '0.170833', '0.188889', '0.220339', '0.236686', '0.278846', '0.305936', '0.32', '0.333333', '0.336842', '0.352941', '0.395062', '0.395062', '0.397436', '0.416667', '0.428571', '0.428571', '0.428571', '0.428571', '0.4375', '0.444444', '0.473684', '0.538462', '0.6', '0.6', '0.6', '0.666667'], ['0.037037', '0.037037', '0.0445434', '0.0504854', '0.0520446', '0.0562414', '0.0725034', '0.0839002', '0.0964912', '0.115578', '0.14245', '0.167975', '0.180435', '0.192678', '0.230556', '0.236686', '0.278846', '0.305936', '0.32', '0.333333', '0.344633', '0.393939', '0.395062', '0.397436', '0.409639', '0.430769', '0.458333', '0.458333', '0.428571', '0.428571', '0.4375', '0.444444', '0.473684', '0.555556', '0.6', '0.6', '0.6', '0.666667'], ['0.037037', '0.037037', '0.0504854', '0.0507614', '0.0532787', '0.0573066', '0.0756303', '0.0899855', '0.115489', '0.125561', '0.151473', '0.171296', '0.192678', '0.213808', '0.232099', '0.259563', '0.278846', '0.305936', '0.327801', '0.344633', '0.355556', '0.393939', '0.397436', '0.409639', '0.430769', '0.468085', '0.468085', '0.458333', '0.44', '0.44', '0.44', '0.444444', '0.52', '0.555556', '0.571429', '0.6', '0.6', '0.6'], ['0.037037', '0.0401606', '0.0507614', '0.0532787', '0.0562414', '0.0695915', '0.0860786', '0.105606', '0.115578', '0.151181', '0.167305', '0.192678', '0.203947', '0.21501', '0.236025', '0.263323', '0.3', '0.315341', '0.344595', '0.352941', '0.355556', '0.393939', '0.423913', '0.431373', '0.454545', '0.468085', '0.487179', '0.468085', '0.458333', '0.444444', '0.444444', '0.52', '0.52', '0.52', '0.555556', '0.555556', '0.6', '0.545455'], ['0.037037', '0.0401606', '0.0507614', '0.0532787', '0.0622776', '0.0695915', '0.0916553', '0.110345', '0.127424', '0.152778', '0.171296', '0.194929', '0.213808', '0.229759', '0.255814', '0.28655', '0.305936', '0.329365', '0.352941', '0.352941', '0.380645', '0.423913', '0.440476', '0.445946', '0.454545', '0.487179', '0.487179', '0.490566', '0.512821', '0.52381', '0.52381', '0.52', '0.52', '0.52', '0.5', '0.545455', '0.571429', '0.666667'], ['0.0401606', '0.0507614', '0.0532787', '0.0621242', '0.0664697', '0.0695915', '0.0972569', '0.111396', '0.127424', '0.152778', '0.17515', '0.197947', '0.21501', '0.242248', '0.28655', '0.3', '0.327801', '0.348315', '0.352941', '0.355556', '0.389381', '0.440476', '0.445946', '0.445946', '0.454545', '0.487179', '0.491803', '0.5', '0.512821', '0.545455', '0.538462', '0.52381', '0.52', '0.5', '0.5', '0.5', '0.666667', '0.666667'], ['0.0546875', '0.0555556', '0.0607595', '0.0640394', '0.0695915', '0.0839065', '0.102828', '0.114068', '0.135616', '0.154977', '0.177922', '0.198093', '0.229759', '0.25', '0.28655', '0.319712', '0.329365', '0.348315', '0.352941', '0.380645', '0.423913', '0.445946', '0.445946', '0.445946', '0.454545', '0.490566', '0.491803', '0.490566', '0.5', '0.5', '0.538462', '0.538462', '0.538462', '0.52', '0.5', '0.6', '0.666667', '0.666667'], ['0.0555556', '0.0555556', '0.0607595', '0.0691928', '0.0740741', '0.0882353', '0.105562', '0.125561', '0.135616', '0.162614', '0.181402', '0.217617', '0.242248', '0.262697', '0.28655', '0.319712', '0.344086', '0.348315', '0.353383', '0.389381', '0.4375', '0.445946', '0.45283', '0.45283', '0.460526', '0.490566', '0.491803', '0.490566', '0.5', '0.5', '0.5', '0.538462', '0.538462', '0.571429', '0.6', '0.666667', '0.666667', '0.666667'], ['0.0555556', '0.0555556', '0.0607595', '0.0728477', '0.0771277', '0.0882353', '0.105562', '0.125561', '0.13738', '0.181373', '0.198093', '0.217617', '0.244932', '0.267797', '0.28655', '0.319712', '0.345515', '0.348315', '0.353383', '0.402597', '0.4375', '0.4375', '0.45283', '0.45283', '0.460526', '0.490566', '0.491803', '0.5', '0.5', '0.5', '0.533333', '0.538462', '0.571429', '0.6', '0.636364', '0.666667', '0.666667', '0.666667'], ['0.0555556', '0.0555556', '0.0640394', '0.0728477', '0.0771277', '0.088968', '0.106646', '0.126062', '0.14827', '0.181402', '0.211988', '0.218629', '0.249389', '0.278281', '0.288416', '0.319712', '0.345515', '0.353383', '0.360825', '0.4375', '0.4375', '0.4375', '0.4375', '0.4375', '0.454545', '0.490566', '0.5', '0.545455', '0.545455', '0.538462', '0.538462', '0.555556', '0.571429', '0.625', '0.636364', '0.666667', '0.75', '0.666667'], ['0.0567686', '0.060241', '0.0640394', '0.0728477', '0.0771277', '0.106646', '0.112853', '0.126062', '0.14881', '0.181402', '0.211988', '0.224165', '0.257009', '0.279605', '0.289199', '0.307116', '0.343915', '0.354286', '0.424', '0.44697', '0.44697', '0.4375', '0.4375', '0.435897', '0.454545', '0.5', '0.545455', '0.555556', '0.555556', '0.548387', '0.555556', '0.555556', '0.571429', '0.625', '0.636364', '1', '1', '1'], ['0.0641026', '0.0640394', '0.0641711', '0.0759494', '0.0974729', '0.110375', '0.11399', '0.131783', '0.14881', '0.181818', '0.208633', '0.227488', '0.257009', '0.288416', '0.295139', '0.307116', '0.343915', '0.39881', '0.44697', '0.44697', '0.45614', '0.45614', '0.45614', '0.45614', '0.468085', '0.5', '0.555556', '0.5625', '0.5625', '0.583333', '0.588235', '0.571429', '0.571429', '0.625', '0.636364', '1', '0.9', '0.9'], ['0.0641026', '0.0641026', '0.0648649', '0.0759494', '0.103565', '0.110375', '0.120321', '0.144876', '0.151724', '0.181818', '0.205397', '0.236655', '0.257009', '0.295139', '0.300885', '0.343915', '0.366197', '0.401274', '0.44697', '0.460674', '0.464789', '0.461538', '0.45614', '0.45614', '0.485714', '0.5', '0.5625', '0.5625', '0.588235', '0.608696', '0.611111', '0.611111', '0.611111', '0.636364', '0.75', '0.75', '0.9', '0.9'], ['0.0641026', '0.0648649', '0.0726257', '0.0802005', '0.106529', '0.110664', '0.137809', '0.14881', '0.161677', '0.185393', '0.205397', '0.239437', '0.257009', '0.295139', '0.334311', '0.365517', '0.371429', '0.401274', '0.453704', '0.460674', '0.461538', '0.461538', '0.464789', '0.485714', '0.5', '0.5', '0.5625', '0.5625', '0.6', '0.608696', '0.611111', '0.611111', '0.666667', '0.666667', '0.8', '1', '1', '1'], ['0.0641026', '0.0726257', '0.0802005', '0.0822622', '0.106529', '0.114286', '0.144876', '0.160428', '0.162242', '0.185393', '0.225', '0.239437', '0.27809', '0.309859', '0.336735', '0.365517', '0.371429', '0.384615', '0.453704', '0.453704', '0.460674', '0.460674', '0.47619', '0.485714', '0.5', '0.5', '0.5625', '0.5625', '0.6', '0.5625', '0.6', '0.666667', '0.666667', '0.666667', '0.8', '1', '1', '1'], ['0.0726257', '0.0802005', '0.0822622', '0.097561', '0.106529', '0.115315', '0.147783', '0.161677', '0.178967', '0.188748', '0.226212', '0.239437', '0.285276', '0.309859', '0.336735', '0.365517', '0.371429', '0.384615', '0.453704', '0.453704', '0.458333', '0.460674', '0.47619', '0.5', '0.5', '0.5', '0.533333', '0.545455', '0.545455', '0.5625', '0.6', '0.6', '0.666667', '0.666667', '0.8', '1', '1', '1']]

def calc_risk(weight, height, age):
  bmi = (weight/2.2)/((height*0.0254)**2)
  # print bmi
  # print  ((array[int(age-20)][int(math.floor(bmi))]))
  # print int(age-20), int(round(bmi,0)), math.floor(100*float(array[int(age-20)][int(round(bmi,0))])*100)/100
  return math.floor(100*float(array[int(age-20)][int(round(bmi-18,0))])*100)/100

def prob_diabetes(user):
  try:
    weight 			= user.reading_set.filter(type="WGHT").order_by("-when")[0].reading
    height 			= user.reading_set.filter(type="HEHT").order_by("-when")[0].reading
    bmi 			= (weight*0.453592)/((height*0.0254)**2)
    current_risk 	= calc_risk(weight, height, user.age)
    plus_10_risk 	= calc_risk(weight, height, user.age + 10)
    age 			=	user.age
    message1 		= """


<p>Your current BMI is %s, and your current risk of diabetes is %s%s </p>
""" % (int(round(bmi,0)), repr(current_risk), "%",)
    message2 = """

<p>In ten years, you will have a %s%s chance of having diabetes
""" % (repr(plus_10_risk), "%",)
    if bmi >= 30:
      message2 += """

 <p>If you lose 10 pounts, that risk would be %s%s</p>
""" % (calc_risk(weight-10, height, age), "%",)
    return message1 + message2
  except:
    return "Please fill out your profile and add weight and height readings to get your BMI risk"

register.filter(prob_diabetes)

# print  calc_risk(220, 66.929, 40)

