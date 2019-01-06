import os
import re

abspath = os.path.abspath(__file__)

print(abspath)

filename = re.split(r'\\|\.', abspath)[-2]

print(filename)