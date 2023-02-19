def get_trace(self):
        '''This returns an abbreviated stack trace with lines that only concern
        the caller. In other words, the stack trace inside the Pexpect module
        is not included. '''

        tblist = traceback.extract_tb(sys.exc_info()[2])
        tblist = [item for item in tblist if ('pexpect/__init__' not in item[0])
                                           and ('pexpect/expect' not in item[0])]
        tblist = traceback.format_list(tblist)
        return ''.join(tblist)