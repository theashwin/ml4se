def read_file(name):
    '''
    output the contents of a file:

    this is a workaround if the cp.push module does not work.
    https://github.com/saltstack/salt/issues/37133

    help the master output the contents of a document
    that might be saved on the minions filesystem.

    .. code-block:: python

        #!/bin/python
        import os
        import salt.client
        s = salt.client.LocalClient()
        o = s.cmd('*', 'highstate_doc.read_file', ['/root/README.md'])
        for m in o:
            d = o.get(m)
            if d and not d.endswith('is not available.'):
                # mkdir m
                #directory = os.path.dirname(file_path)
                if not os.path.exists(m):
                    os.makedirs(m)
                with open(m + '/README.md','wb') as fin:
                    fin.write(d)
                print('ADDED: ' + m + '/README.md')
    '''
    out = ''
    try:
        with salt.utils.files.fopen(name, 'r') as f:
            out = salt.utils.stringutils.to_unicode(f.read())
    except Exception as ex:
        log.error(ex)
        return None
    return out