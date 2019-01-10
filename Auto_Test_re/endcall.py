from configs import *
from phones import *
from status import *

import os
import time

phoneA = p_list[0]
phoneB = p_list[1]
# phone_c = p_list[2]


# cur_exec_files = os.path.basename(__file__)
# log_level = 'info'
# screen_path = init_logging(cur_exec_files, log_level)

cmd_answer = ['OK', 'SPEAKER', 'F1']
cmd_end = ['X', 'SPEAKER', 'F4']


for cd1, cd2 in zip(cmd_answer, cmd_end):
    phoneA.dial(phoneB.ext)
    time.sleep(2)
    phoneB.answer(cd1)
    phoneB.end_call(cd2)


    phoneB.dial(phoneA.ext)
    time.sleep(2)
    phoneA.answer(cd1)
    phoneA.end_call(cd2)

    phoneA.get_memory()
    phoneB.get_memory()
# s.set_status('idle', ip_1='10.3.2.22', ip2='10.3.2.23')
# set_idle_status()
# check_status('idle', dut_a.ip)