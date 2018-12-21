import EndCall


cmd = ['F4', 'SPEAKER']
# edc_cmd = 'SPEAKER'
# edc_cmd = 'F4'


test_loops = 1
for loop in range(test_loops):
    for edc_cmd in cmd:
        EndCall.DUT_A(loop, edc_cmd)
        EndCall.DUT_B(loop, edc_cmd)
        print(loop)
        if (loop + 1) == test_loops:
            EndCall.logging.info('All --[' + str(test_loops) + ' Test Loops]-- Ended.')
        else:
            EndCall.logging.info('The next loop --[Test Loop ' + str(loop + 1) + ']-- Start')
