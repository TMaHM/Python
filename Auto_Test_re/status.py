import requests
import re

from configs import *

def set_idle_status(*kw):

    result = False
    if kw:
        for ip in kw:
            url = Test_url(ip)
            url_f4 = url.keyboard + 'F4'
            url_x = url.keyboard + 'X'
            log.info('Try to set [idle] status in ' + ip)
            try:
                r_f4 = requests.get(url_f4, timeout=1)
                r_x = requests.get(url_x, timeout=1)
                if r_f4 == r_x == 200:
                    log.info(ip + ' set [idle] status success.')
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
    pat_retrun = r'(?<=<Return>)(\d)(?=</Return>)'
    pat_status = r'([a-zA-Z]+State=.*)(?=\<)'
    if kw:
        for ip in kw:
            url = Test_url(ip)
            code = P_Status(status)['code']
            url_check = url.check_status + code
            log.info('Try to check status [' + status + '] in ' + ip)
            try:
                r_status = requests.get(url_check, timeout=1)
                if r_status.status_code == 200:
                    return_code = re.findall(pat_retrun, r_status.text)
                    if return_code == '1':
                        log.info('Check Error, Return code 1...')
                        return_status = re.findall(pat_status, r_status.text)
                        for key,value in
                    log.info('Check success...')
                    result = True
                else:
                    log.info('Return ' + str(r_status.status_code) + '. Check failed...')

            except requests.exceptions.ConnectionError:
                log.info('Connect Error...Check failed...')
    else:
        print('No necessary parameters: IP')
    return result


def judge_status(status, ip):
    url = Test_url(ip)
    url_judge = url.check_status + status
    log.info('Try to judge status in ' + ip)
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

