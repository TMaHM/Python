from transfer import *

pA = Phone('10.3.2.72', extension='074')
pB = Phone('10.3.2.73', extension='075')
pC = Phone('10.3.2.74', extension='076')
pD = Phone('10.3.2.22')

attended_Transfer(pA, pB, pC)
# semi_Attended_Transfer(pA, pB, pC)
# blind_Transfer(pA, pB, pC)