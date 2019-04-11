import re


with open('temp.xml', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for eachLine in lines:
        r = re.split(r'\s', eachLine)
        # print(r)
        with open('phonebook.xml', 'a', encoding='utf-8') as f1:
            if len(r) >= 6:
                f1.write('<contact sDisplayName="' + r[1] + '" sOfficeNumber="' + r[0] + '" sMobilNumber="' + r[4] + '" sOtherNumber="' + r[5] + '" sAccountIndex="0" sRing="Auto" group="" photoDefault="" photoSelect="0" />' + '\n')