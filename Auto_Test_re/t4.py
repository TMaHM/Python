import re

dsskey_dir = {
    'l1':{'type':'LineKey1_Type', 'value':'LineKey1_Value', 'account':'LineKey1_Account'},
}

key_type_code_dir = {
    'blf':'3'
}

key_account_code_dir = {
    'account1':'0'
}

def set_key(key, type, value, account='Account1'):

    # if key == 'l1':
    pat_key_type = dsskey_dir[key]['type']
    pat_key_value = dsskey_dir[key]['value']
    pat_key_account = dsskey_dir[key]['account']

    pat_pv = r'(?<=<)(P\d+)'

    with open('cfg.xml', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for eachline in lines:
            key_type = re.findall(pat_key_type, eachline)
            key_value = re.findall(pat_key_value, eachline)
            key_account = re.findall(pat_key_account, eachline)
            if key_type:
                pv_key_type = re.findall(pat_pv, eachline)[0]
                print(pv_key_type)
            if key_value:
                pv_key_value = re.findall(pat_pv, eachline)[0]
                print(pv_key_value)
            if key_account:
                pv_key_account = re.findall(pat_pv, eachline)[0]
                print(pv_key_account)


    pc_type = key_type_code_dir[type.lower()]
    pc_account = key_account_code_dir[account.lower()]

    print(pc_type)
    print(pc_account)


set_key('l1', 'blf', '2051')