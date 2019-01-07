import os
import re
import logging as log

num_dut = 5

ip1 = '10.3.2.22'
ip2 = '10.3.2.19'
ip3 = '10.3.2.24'
ip4 = '10.3.2.25'
ip5 = '10.3.2.26'

ext1 = '8724'
ext2 = '3207'
ext3 = '8760'
ext4 = '8811'
ext5 = '8921'

ip_list = [ip1, ip2, ip3, ip4, ip5]
ext_list = [ext1, ext2, ext3, ext4, ext5]

p_list = []



def init_logging(cur_exec_file, log_level='info'):
    # 当前执行文件的文件名
    # 当前所在目录的路径
    root_path = os.path.dirname(__file__)
    # 去除文件名后缀，用作建立当前执行文件的log存放目录
    cur_exec_file_nosuffix = re.split(r'\.', cur_exec_file)[0]
    # log及截屏文件存放目录
    log_dir_path = root_path + '\\log\\' + cur_exec_file_nosuffix + '\\'
    # log文件绝对路径
    log_file = log_dir_path + cur_exec_file_nosuffix + '.log'
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)

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
t = 'hello'
t.lower()

class Test_url():
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

class P_Status():
    def __init__(self, status):
        self.status = status
        # idle = {'code': '0', 'status':['FXSState=0x80', 'CallCtlState=0x60', 'LCMState=-1 ']}
        # speaker = {'code': '1', 'status':['FXSState=0x81', 'CallCtlState=0x61', 'LCMState=4 ']}
        # outgoing = {'code': '1', 'status':['FXSState=0x82', 'CallCrtlState=0x62', 'LCMState=5 ']}
        {
            'idle':'0', ['FXSState=0x80','CallCtlState=0x60','LCMState=-1 ']:'[idle]',
            'speaker':'1', ['FXSState=0x81', 'CallCtlState=0x61', 'LCMState=4 ']:'[Speaker]',
            'outgoing':'1'
        }
        return
        if self.status.lower() == 'idle':
            return idle


        self.ps_List = [idle, speaker]

# phone_status_dir = {
#     'idle': [{'code': '0'},
#              {'FXSState': '0x80', 'CallCtlState': '0x60',
#               'LCMState': '-1'}],
#     'speaker': [{'code': '1'},
#                 {'FXSState': '0x81', 'CallCtlState': '0x61',
#                  'LCMState': '4'}],
#     'outgoing': [{'code': '2'},
#                  {'FXSState': '0x82', 'CallCtlState': '0x62',
#                   'LCMState': '5'}],
#     'talking': [{'code': '3'},
#                 {'FXSState': '0x82', 'CallCtlState': '0x64',
#                  'LCMState': '6'}],
#     'ringing': [{'code': '4'},
#                 {'FXSState': '0x82', 'CallCtlState': '0x63',
#                  'LCMState': '3'}],
#     'hold': [{'code': '5'},
#              {'FXSState': '0x82', 'CallCtlState': '0x87',
#               'LCMState': '7'}],
#     'new_initiate': [{'code': '6'},
#                      {'FXSState': '0x82', 'CallCtlState': '0x81',
#                       'LCMState': '11'}],
#     'new_talking': [{'code': '7'},
#                     {'FXSState': '0x82', 'CallCtlState': '0x82',
#                      'LCMState': '6'}],
#     'conference': [{'code': '8'},
#                    {'FXSState': '0x82', 'CallCtlState': '0x88',
#                     'LCMState': '9'}],
#     'conf_held': [{'code': '9'},
#                   {'FXSState': '0x82', 'CallCtlState': '0x8d',
#                    'LCMState': '9'}],
#     'check_ok': [{'code': '0'},
#                  {'FXS': '0', 'CallCtl': '0', 'LCM': '0'}],
# }
