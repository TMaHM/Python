import requests

from configs import *

def set_idle_status(*kw):

    result = False
    if kw:
        for ip in kw:
            url = TestUrl(ip)
            url_return_idle = url.prefix + 'drd=RETURNIDLE'
            # log.info('Try to set [idle] status in ' + ip)
            try:
                r_return_idle = requests.get(url_return_idle, timeout=1)
                if r_return_idle.status_code == 200:
                    log.info(ip + ' set [idle] status in ' + ip + ' success.')
                    result = True
                else:
                    log.info('Press F4 return ' + r_return_idle.status_code)
            except requests.exceptions.ConnectionError:
                log.info('Connect Error...Set [idle] status failed...')
    else:
        print("No necessary parameters: IP")
    return result

def check_status(status, *kw):

    result = False
    pat_return = r'(?<=<Return>)(\d)(?=</Return>)'
    pat_status = r'([a-zA-Z]+State=.*)(?=\<)'
    pat_ok = r'(?<=\>)(.*)(?=\<)'
    if kw:
        for ip in kw:
            url = TestUrl(ip)
            code = p_status(status)
            url_check = url.check_status + code
            # log.info('Try to check status [' + status + '] in ' + ip)
            try:
                r_status = requests.get(url_check, timeout=1)
                if r_status.status_code == 200:
                    return_code = re.findall(pat_return, r_status.text)
                    print(return_code)
                    if return_code == ['1']:
                        log.info('Check [' + status + '] Error, Return code 1...')
                        return_status = re.findall(pat_status, r_status.text)
                        match_status = p_status(return_status)
                        if match_status == None:
                            log.info('The Phone is now ' + str(return_status))
                        else:
                            log.info('The Phone is now in ' + match_status)
                    elif return_code == ['0']:
                        return_status = re.findall(pat_ok, r_status.text)
                        print(return_status)
                        if return_status == ['0', '0', '0', '0']:
                            log.info('Check status [' + status + '] success...')
                            result = True
                        else:
                            log.info('Check Error...')
                            log.info(r_status.text)
                    elif return_code == None:
                        log.info('Unknown Status...')
                        log.info(r_status.text)
                else:
                    log.info('Return ' + str(r_status.status_code) + '. Check failed...')

            except requests.exceptions.ConnectionError:
                log.info('Connect Error...Check failed...')
    else:
        print('No necessary parameters: IP')
    return result
