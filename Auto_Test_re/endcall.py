from phones import *

import time

# pA = p_list[0]
# pB = p_list[1]
# phone_c = p_list[2]


pA = Phone('10.3.2.22', extension='8724')
pB = Phone('10.3.2.15', extension='3206', pwd='222222')


cmd_answer = ['OK', 'SPEAKER', 'F1']
cmd_end = ['X', 'SPEAKER', 'X']


for cd1, cd2 in zip(cmd_answer, cmd_end):
    pA.dial(pB.ext)
    time.sleep(2)
    pB.answer(cd1)
    pB.end_call(cd2)


    pB.dial(pA.ext)
    time.sleep(2)
    pA.answer(cd1)
    pA.end_call(cd2)

    pA.get_memory()
    pB.get_memory()