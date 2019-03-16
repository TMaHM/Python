import re

pattern = r'(<P.*>).*(</.*>)'


with open('temp.txt', 'r', encoding='utf-8') as f:
    with open('temp.xml', 'a+', encoding='utf-8') as f1:
        content = f.readlines()

        for sentence in content:
            number = re.findall(r'(?<="LineKey)(\d+)\.', sentence)
            flag = re.findall(r'(?<=\.)(.*)\"', sentence)
            if number != []:
                tag = number[0]
                tabel = flag[0]
                # print(number)
            group = re.findall(pattern, sentence)
            if group != []:
                # print(group)
                s1 = group[0][0]
                s2 = group[0][1]
                if tabel == 'PickupCode':
                    f1.write('\t\t' + s1 + '*97' + s2 + '\n')
                else:
                    f1.write('\t\t' + s1 + '%TT_H_LK' + tag + '_' + tabel.upper() + '%' + s2 + '\n')
            else:
                f1.write(sentence)


