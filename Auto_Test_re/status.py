import requests

from phones import Phone
from configs import *


def set_idle_status(*kw):

    result = False
    if kw:
        for ip in kw:
            url_f4 = Phone(ip).url_keyboard + 'F4'
            url_x = Phone(ip).url_keyboard + 'X'
            log.info('Try to set [idle] status in ' + ip)
            try:
                r_f4 = requests.get(url_f4, timeout=1)
                r_x = requests.get(url_x, timeout=1)
                if r_f4 == r_x == 200:
                    log.info(ip + ' set [idle] status successfully.')
                    result = True
                else:
                    log.info('Press F4 return ' + r_f4.status_code)
                    log.info('Press X return ' + r_x.status_code)
                    judge_status(ip)
            except requests.exceptions.ConnectionError:
                log.info('Connect Error...Set [idle] status failed...')
    else:
        ip = None
        print("No necessary parameters: IP")
    return result

def check_status(status, *kw):

    result = False
    if kw:
        for ip in kw:
            url_check = Phone(ip).url_check_status + status
            log.info('Try to check status [' + status + '] with ' + url_check)
            try:
                r_status = requests.get(url_check, timeout=1)
                if r_status == 200:
                    log.info('Check successfully...')
                    result = True
                else:
                    log.info('Return ' + str(r_status.status_code) + '. Check failed...')

            except requests.exceptions.ConnectionError:
                log.info('Connect Error...Judge failed...')
    else:
        print('No necessary parameters: IP')
    return result


def judge_status(status, ip):

    url_judge = Phone(ip).url_check_status + status
    log.info('Try to judge status with ' + url_judge)
    try:
        r_judge = requests.get(url_judge, timeout=1)
        if r_judge.status_code == 200:
            log.info(ip + ' is now in ' + status)
            result = True
        else:
            log.info('Return ' + str(r_judge.status_code) + '. Judge failed...')

    except requests.exceptions.ConnectionError:
        log.info('Connect Error...Judge failed...')

    return status

