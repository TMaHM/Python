import os
import logging as log

# 定义话机状态字典，用于status.py，设置idle态及check状态
p_status_dir = \
    {
        '0': 'idle', '[idle]': ['FXSState=0x80', 'CallCtlState=0x60', 'LCMState=-1 '],
        '1': 'speaker', '[Speaker]': ['FXSState=0x81', 'CallCtlState=0x61', 'LCMState=4 '],
        '2': 'outgoing', '[Outgoing]': ['FXSState=0x82', 'CallCtlState=0x62', 'LCMState=5 '],
        '3': 'talking', '[Talking]': ['FXSState=0x82', 'CallCtlState=0x64', 'LCMState=6 '],
        '4': 'ringing', '[Ringing]': ['FXSState=0x82', 'CallCtlState=0x63', 'LCMState=3 '],
        '5': 'hold', '[Hold]': ['FXSState=0x82', 'CallCtlState=0x87', 'LCMState=7 '],
        '6': 'new_initiate', '[New_Init]': ['FXSState=0x82', 'CallCtlState=0x81', 'LCMState=11 '],
        '7': 'new_talking', '[New_Talking]': ['FXSState=0x82', 'CallCtlState=0x82', 'LCMState=6 '],
        '8': 'conference', '[Conference]': ['FXSState=0x82', 'CallCtlState=0x88', 'LCMState=9 '],
        '9': 'conf_hold', '[Conf_Hold]': ['FXSState=0x82', 'CallCtlState=0x8d', 'LCMState=9 '],
    }

exp_blf_dir = \
    {
        'L1' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:0',
        'L2' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:1',
        'L3' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:2',
        'L4' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:3',
        'L5' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:4',
        'L6' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:5',
        'L7' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:6',
        'L8' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:7',
        'L9' : 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:8',
        'L10': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:9',
        'L11': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:10',
        'L12': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:11',
        'L13': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:12',
        'L14': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:13',
        'L15': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:14',
        'L16': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:15',
        'L17': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:16',
        'L18': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:17',
        'L19': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:18',
        'L20': 'EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:19',
    }

dsskey_dir = {}

for i in range(1, 37):
    dsskey_dir['l' + str(i)] = {'type'   : 'linekey' + str(i) + '_type', 'value': 'linekey' + str(i) + '_value',
                                'account': 'linekey' + str(i) + '_account', 'label': 'linekey' + str(i) + '_label', }

key_type_code_dir = {
    'N/A'                : '0',
    'LINE'               : '1',
    'SPEEDDIAL'          : '2',
    'BLF'                : '3',
    'BLF LIST'           : '4',
    'VOICEMAIL'          : '5',
    'DIRECT PICKUP'      : '6',
    'GROUP PICKUP'       : '7',
    'CALL PARK'          : '8',
    'INTERCOM'           : '9',
    'DTMF'               : '10',
    'PREFIX'             : '11',
    'LOCAL GROUP'        : '12',
    'XML GROUP'          : '13',
    'XML BROWSER'        : '14',
    'LDAP'               : '15',
    'NETWORK DIRECTORIES': '16',
    'CONFERENCE'         : '17',
    'FORWARD'            : '18',
    'TRANSFER'           : '19',
    'HOLD'               : '20',
    'DND'                : '21',
    'REDIAL'             : '22',
    'CALL RETURN'        : '23',
    'SMS'                : '24',
    'RECORD'             : '25',
    'URL RECORD'         : '26',
    'PAGING'             : '27',
    'GROUP LISTENING'    : '28',
    'PUBLIC HOLD'        : '29',
    'PRIVATE HOLD'       : '30',
    'HOT DESKING'        : '32',
    'ACD'                : '33',
    'ZERO TOUCH'         : '34',
    'URL'                : '35',
    'NETWORK GROUP'      : '44',
    'MULTICAST PAGING'   : '47',
    'GROUP CALL PARK'    : '51',
    'CALLPARK RETRIEVE'  : '52',
    'PULL CALL'          : '53'}

key_account_code_dir = {
    'ACCOUNT1': '0',
    'ACCOUNT2': '1',
    'ACCOUNT3': '2',
    'ACCOUNT4': '3',
    'ACCOUNT5': '4',
    'ACCOUNT6': '5',
}


def init_log(log_level='info'):
    """
    在具体文件执行初始化log参数
    :param log_level: log等级，默认为info
    :return: log及截图存放目录 --> log_dir_path
    """
    # 当前所在目录的路径
    root_path = os.path.dirname(__file__)
    # log及截屏文件存放目录
    # log_dir_path = root_path + '\\log\\' + cur_exec_file_nosuffix + '\\'
    log_dir = root_path + '\\log\\'
    screen_dir = log_dir + 'screenShot\\'
    # log文件绝对路径
    log_file = log_dir + 'atlog.log'
    screen_file = screen_dir

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)

    if log_level == 'debug':
        log.basicConfig(level=log.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%b %d %H:%M:%S',
                        filename=log_file,
                        filemode='a')
    elif log_level == 'info':
        log.basicConfig(level=log.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%b %d %H:%M:%S',
                        filename=log_file,
                        filemode='a')
    return screen_file


init_log()


class TestUrl:
    """
    通用型URL的集合，提供给Phone类调用，部分需要附加参数
    ip: Phone的IP
    usr&pwd: 默认admin，需要改变时传入相应参数
    Usage::
        见phones 14行
    """

    def __init__(self, ip, usr='admin', pwd='admin'):
        self.ip = ip
        self.usr = usr
        self.pwd = pwd

        self.prefix = 'http://' + self.usr + ':' + self.pwd + '@' + self.ip

        self.screenshot = self.prefix + '/download_screen'
        self.keyboard = self.prefix + '/AutoTest&keyboard='
        self.check_status = self.prefix + '/AutoTest&autoverify=STATE='
        self.get_memory = self.prefix + '/AutoTest&autoverify=MEMORYFREE'
        self.setting = self.prefix + '/AutoTest&setting='


def p_status(status):
    """
    通过传入的话机状态的参数，匹配p_status_dir字典
    :param status: 要check的话机状态，如idle，提供给check_status调用，匹配状态字典中的值
    :return: 根据传入的参数，返回话机当前状态码或状态名
    Usage::
        status = 'idle'
        code = p_status(status) -> 返回状态对应的url末尾的检查码
        status = ['FXSState=0x82', 'CallCtlState=0x8d', 'LCMState=9 ']
        -> 返回对应的状态名
    """
    if status in p_status_dir.values():
        for key, value in p_status_dir.items():
            if status == value:
                return key
    else:
        return None
