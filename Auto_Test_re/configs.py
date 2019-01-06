import os
import re
import logging as log
# from phones import Phone

ip1 = '10.3.2.22'
ip2 = '10.3.2.23'
ip3 = '10.3.2.24'
ip4 = '10.3.2.25'
ip5 = '10.3.2.26'

ip_list = [ip1, ip2, ip3, ip4, ip5]

ext1 = '8724'
ext2 = '8759'
ext3 = '8760'
ext4 = '8811'
ext5 = '8921'

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