from configs import *
from phones import *
from status import *


import os

dut_a = p_list[0]
dut_b = p_list[1]


cur_exec_files = os.path.basename(__file__)
log_level = 'info'
print(cur_exec_files)
# dut_a.init_logging(cur_exec_files, log_level)
init_logging(cur_exec_files, log_level)


dut_a.dial(dut_b.ext)
dut_b.answer()
dut_b.end_call('X')
dut_a.get_memory()
dut_a.screen_shot()

# s.set_status('idle', ip_1='10.3.2.22', ip2='10.3.2.23')
set_idle_status()
check_status('idle', dut_b.ip)
judge_status('idle', dut_b.ip)