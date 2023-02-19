def _sendto(self, data, addr=None, attempts=10):
        '''
        On multi-master environments, running on the same machine,
        transport sending to the destination can be allowed only at once.
        Since every machine will immediately respond, high chance to
        get sending fired at the same time, which will result to a PermissionError
        at socket level. We are attempting to send it in a different time.

        :param data:
        :param addr:
        :return:
        '''
        tries = 0
        slp_time = lambda: 0.5 / random.randint(10, 30)
        slp = slp_time()
        while tries < attempts:
            try:
                self.transport.sendto(data, addr=addr)
                self.log.debug('Sent successfully')
                return
            except AttributeError as ex:
                self.log.debug('Permission error: %s', ex)
                time.sleep(slp)
                tries += 1
                slp += slp_time()