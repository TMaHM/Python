import configurations as conf


def test_call(ip, command=None, ext=None):
    if command == None and ext != None:
        url_tc = conf.Url(ip).url_setting + 'P4210=' + 'test' + ext
        print(url_tc)

    elif command == 's':
        url_tc = conf.Url(ip).url_setting + 'P4210=' + ''
        print(url_tc)

    else:
        print('param error.')



test_call('10.10.2.2', 's')
test_call('10.10.3.3', ext='67')
test_call('10.10.4.4')
test_call('10.10.5.5', 's', ext='88')