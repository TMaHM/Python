# with open(r'C:\Users\ywbhs\Desktop\Language\19_Nederlands(Dutch).xml', 'r', encoding='utf-8') as f:
#     fomatDoc = f.readlines()
#
#     with open(r'C:\Users\ywbhs\Desktop\901_902\Language\19_Nederlands(Dutch).xml', 'r', encoding='utf-8') as fe:
#         editDoc = fe.readlines()
#
#         with open(r'language.xml', 'a+', encoding='utf-8') as final_doc:
#             for line in editDoc:
#                 if line in fomatDoc:
#                     final_doc.write(line)
#                 else:
#                     print(line)
import re
import collections

keys = collections.OrderedDict()
pat_key = r'(".*")(?=\s?:)'
pat_value = r'\s?:\s?".*",'

with open(r'E:\svn\voip_res\OEM\RoutIT\Language\802，802T，803,804,806,601,901,902_language\Language\19_Dutch.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if r'//' in line or r'/\*.*\*/' in line:
            keys[line] = ''
        else:
            key = re.search(pat_key, line)
            # print(key)
            value = re.search(pat_value, line)
            if key and value:
                keys[key[0]] = value[0]
        # print(content)

with open(r'language_key.js', 'a+', encoding='utf-8') as f:
    for k, v in keys.items():
        # print(k, v)
        if v != '':
            f.write('\t' + k + v + '\n')
        else:
            f.write(k)