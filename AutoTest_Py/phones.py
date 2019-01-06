class Phone111():
    """定义Phone类，通过参数赋予Phone各种属性，并转为url\n
    共有5个参数，类型都为str\n
    其中ip必须给定，其他4个参数account, number, usr, pwd有默认值，在需要时提供\n
    如果要调用url_dial，则必须提供number\n
    Usage::
        >>> from phones import Phone111
        >>> import requests
        >>> dut_1 = Phone111(ip='10.3.2.22', number='8724')
        >>> dut_1_f4 = dut_1.url_keyboard + 'F4'
        >>> r_1_f4 = requests.get(dut_1_f4)
        >>> dut_1_dial = dut_1.url_dial
    """
    def __init__(self, ip, account='Account=1', number=None, usr='admin', pwd='admin'):
        self.ip = ip
        self.usr = usr
        self.pwd = pwd
        self.account = account
        self.number = number

        self.url_gen_prefix = 'http://' + self.usr + ':' + self.pwd + '@' + self.ip

        if self.number:
            self.url_dial = self.url_gen_prefix + '/Phone_ActionURL&Command=1&Number=' + self.number + '&' + \
                            self.account

        self.url_screenshot = self.url_gen_prefix + '/download_screen'
        self.url_keyboard = self.url_gen_prefix + '/AutoTest&keyboard='
        self.url_check_status = self.url_gen_prefix + '/AutoTest&autoverify=STATE='
        self.url_get_memory = self.url_gen_prefix + '/AutoTest&autoverify=MEMORYFREE'
        self.url_setting = self.url_gen_prefix + '/AutoTest&setting='

