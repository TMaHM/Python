with open(r'C:\Users\ywbhs\Desktop\Language\19_Nederlands(Dutch).xml', 'r', encoding='utf-8') as f:
    fomatDoc = f.readlines()

    with open(r'C:\Users\ywbhs\Desktop\901_902\Language\19_Nederlands(Dutch).xml', 'r', encoding='utf-8') as fe:
        editDoc = fe.readlines()

        with open(r'language.xml', 'a+', encoding='utf-8') as final_doc:
            for line in editDoc:
                if line in fomatDoc:
                    final_doc.write(line)
                else:
                    print(line)