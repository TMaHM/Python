import os, time
from p_functions import PhoneFunction
import configurations as conf
import logging


ip_A = '10.3.2.19'
ip_B = '10.3.2.22'

ext_A = '3207'
ext_B = '8724'

status = 'idle'
cmd = ['F4', 'SPEAKER']

basename = os.path.basename(__file__)
pf = PhoneFunction(basename, 'info')
logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%b %d %H:%M:%S',
                        filename=pf.log_file,
                        filemode='a')


def DUT_A(loop, edc_cmd):
    if loop == 0:
        logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- Start')
    # 设置两台DUT为idle态
    check_A = pf.idle_state_set(ip_A)
    check_B = pf.idle_state_set(ip_B)
    # 检查返回状态，之后必须sleep 1-2s，留给GUI反应时间
    if check_A and check_B :
        time.sleep(1)
        # 拨号并保持3s
        pf.dial(ip_A, ext_B)
        time.sleep(2)
        # answer并check talking status，如果check ok，保持2s --> 实际会有2-3s时间
        answer = pf.answer(ip_B, ip_A)
        if answer:
            time.sleep(1)
            # 结束通话，并check idle status，sleep 1s，留给GUI反应时间 --> 视话机而言，至少对黑白屏不需要
            endcall = pf.endcall(ip_A, ip_B, edc_cmd)
            if endcall:
                logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- A call B end, continue...')
                return True
            else:
                logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- A call B failed in end call.')
                return False
        else:
            logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- A call B failed in answer the call.')
            return False
    else:
        return False


def DUT_B(loop, edc_cmd):
    check_A = pf.idle_state_set(ip_B)
    check_B = pf.idle_state_set(ip_A)
    if check_A and check_B:
        time.sleep(1)
        pf.dial(ip_B, ext_A)
        time.sleep(2)
        answer = pf.answer(ip_A, ip_B)
        if answer:
            time.sleep(2)
            endcall = pf.endcall(ip_B, ip_A, edc_cmd)
            if endcall:
                logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- Ended successfully.')
                return True
            else:
                logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- B call A failed in end call.')
                return False
        else:
            logging.info(pf.cur_exec_file_nosuffix + edc_cmd + ' --[Test Loop ' + str(loop) + ']-- B call A failed in answer the call.')
            return False
    else:
        return False


test_loops = 1
for loop in range(test_loops):
    for edc_cmd in cmd:
        DUT_A(loop, edc_cmd)
        DUT_B(loop, edc_cmd)
        print(loop)
        if (loop + 1) == test_loops:
            logging.info('All --[' + str(test_loops) + ' Test Loops]-- Ended.')
        else:
            logging.info('The next loop --[Test Loop ' + str(loop + 1) + ']-- Start')
