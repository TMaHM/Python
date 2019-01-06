class Phone():
    def __init__(self, ip, extension, account='Account=1', usr='admin', pwd='admin'):
        self.ip = ip
        self.ext = extension
        self.account = account
        self.usr = usr
        self.pwd = pwd
        self.url()

    def url(self):
        self.url_gen_prefix = 'http://' + self.usr + ':' + self.pwd + '@' + self.ip

        if self.ext:
            self.url_dial = self.url_gen_prefix + '/Phone_ActionURL&Command=1&Number=' + self.ext + '&' + \
                            self.account

        self.url_screenshot = self.url_gen_prefix + '/download_screen'
        self.url_keyboard = self.url_gen_prefix + '/AutoTest&keyboard='
        self.url_check_status = self.url_gen_prefix + '/AutoTest&autoverify=STATE='
        self.url_get_memory = self.url_gen_prefix + '/AutoTest&autoverify=MEMORYFREE'
        self.url_setting = self.url_gen_prefix + '/AutoTest&setting='
