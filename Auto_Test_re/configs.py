import os
import re
import logging as log

# 定义执行话机总数，在phones.py中实例化
num_dut = 5

# 定义DUT的IP
ip1 = '10.3.2.22'
ip2 = '10.3.2.19'
ip3 = '10.3.2.24'
ip4 = '10.3.2.25'
ip5 = '10.3.2.26'

# 定义DUT的ext --> 与IP一一对应
ext1 = '8724'
ext2 = '3207'
ext3 = '8760'
ext4 = '8811'
ext5 = '8921'

ip_list = [ip1, ip2, ip3, ip4, ip5]
ext_list = [ext1, ext2, ext3, ext4, ext5]

# 定义话机列表，方便在具体脚本中赋值
p_list = []

# 定义话机状态字典，用于status.py，设置idle态及check状态
p_status_dir = \
    {
        '0':'idle', '[idle]':['FXSState=0x80', 'CallCtlState=0x60', 'LCMState=-1 '],
        '1':'speaker', '[Speaker]':['FXSState=0x81', 'CallCtlState=0x61', 'LCMState=4 '],
        '2':'outgoing', '[Outgoing]':['FXSState=0x82', 'CallCtlState=0x62', 'LCMState=5 '],
        '3':'talking', '[Talking]':['FXSState=0x82', 'CallCtlState=0x64', 'LCMState=6 '],
        '4':'ringing', '[Ringing]':['FXSState=0x82', 'CallCtlState=0x63', 'LCMState=3 '],
        '5':'hold', '[Hold]':['FXSState=0x82', 'CallCtlState=0x87', 'LCMState=7 '],
        '6':'new_initiate', '[New_Init]':['FXSState=0x82', 'CallCtlState=0x81', 'LCMState=11 '],
        '7':'new_talking', '[New_Talking]':['FXSState=0x82', 'CallCtlState=0x82', 'LCMState=6 '],
        '8':'conference', '[Conference]':['FXSState=0x82', 'CallCtlState=0x88', 'LCMState=9 '],
        '9':'conf_hold', '[Conf_Hold]':['FXSState=0x82', 'CallCtlState=0x8d', 'LCMState=9 '],
    }


def init_log(cur_exec_file, log_level='info'):
    """
    在具体文件执行初始化log参数
    :param cur_exec_file: 当前执行文件名，通过文件头执行os.path.basename(__file__)获得
    :param log_level: log等级，默认为info
    :return: log及截图存放目录 --> log_dir_path
    Usage::
        >>> cur_exec_files = os.path.basename(__file__)
        >>> log_level = 'info'
        >>> init_logging(cur_exec_files, log_level)
    """
    # 当前所在目录的路径
    root_path = os.path.dirname(__file__)
    # 去除文件名后缀，用作建立当前执行文件的log存放目录
    cur_exec_file_nosuffix = re.split(r'\.', cur_exec_file)[0]
    # log及截屏文件存放目录
    # log_dir_path = root_path + '\\log\\' + cur_exec_file_nosuffix + '\\'
    log_dir = root_path + '\\log\\'
    screen_dir = log_dir + 'screenshot\\'
    # log文件绝对路径
    log_file = log_dir + 'atlog.log'
    screen_file = screen_dir + cur_exec_file_nosuffix

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


class Test_Url():
    """
    通用型URL的集合，提供给Phone类调用，部分需要附加参数
    ip: Phone的IP
    usr&pwd: 默认admin，需要改变时传入相应参数
    Usage::
        >>> 见phones 14行
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
        >>> status = 'idle'
        >>> code = p_status(status) --> 返回状态对应的url末尾的检查码
        >>> status = ['FXSState=0x82', 'CallCtlState=0x8d', 'LCMState=9 ']
        >>> --> 返回对应的状态名
    """
    if status in p_status_dir.values():
        for key,value in p_status_dir.items():
            if status == value:
                return key
    else:
        return None
#     'check_ok': [{'code': '0'},
#                  {'FXS': '0', 'CallCtl': '0', 'LCM': '0'}],
# }
