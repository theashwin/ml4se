def start(vm, options=None, key='uuid'):
    '''
    Start a vm

    vm : string
        vm to be started
    options : string
        optional additional options
    key : string [uuid|alias|hostname]
        value type of 'vm' parameter

    CLI Example:

    .. code-block:: bash

        salt '*' vmadm.start 186da9ab-7392-4f55-91a5-b8f1fe770543
        salt '*' vmadm.start 186da9ab-7392-4f55-91a5-b8f1fe770543 'order=c,once=d cdrom=/path/to/image.iso,ide'
        salt '*' vmadm.start vm=nacl key=alias
        salt '*' vmadm.start vm=nina.example.org key=hostname
    '''
    ret = {}
    if key not in ['uuid', 'alias', 'hostname']:
        ret['Error'] = 'Key must be either uuid, alias or hostname'
        return ret
    vm = lookup('{0}={1}'.format(key, vm), one=True)
    if 'Error' in vm:
        return vm
    # vmadm start <uuid> [option=value ...]
    cmd = 'vmadm start {uuid} {options}'.format(
        uuid=vm,
        options=options if options else ''
    )
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = res['stderr'] if 'stderr' in res else _exit_status(retcode)
        return ret
    return True